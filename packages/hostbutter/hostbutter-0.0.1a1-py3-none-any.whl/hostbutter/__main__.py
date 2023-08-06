import os
import subprocess
import sys
from contextlib import suppress
from typing import Any, Optional

import myke
import yapx

from .__version__ import __version__
from .actions import ClusterAction, SwarmAction
from .utils import chdir, setenv, switch_context

ANSIBLE_COLLECTION_DIR: str = os.path.join(os.path.dirname(__file__), "collections")
ANSIBLE_REQUIREMENTS_FILE: str = os.path.join(
    ANSIBLE_COLLECTION_DIR, "requirements.yml"
)


def setup(
    context: Optional[str] = yapx.arg(None, env="DOCKER_CONTEXT"),
    inventory_dir: str = yapx.arg(
        os.path.join(os.path.expanduser("~"), ".hostbutter"),
        env="HOSTBUTTER_CONFIG_DIR",
    ),
):
    context_before: str | None = os.getenv("DOCKER_CONTEXT")

    if not context_before:
        with suppress(FileNotFoundError):
            docker_conf: dict[str, Any] = myke.read.json(
                os.getenv(
                    "DOCKER_CONFIG",
                    os.path.join(os.path.expanduser("~"), ".docker", "config.json"),
                )
            )
            context_before = docker_conf.get("currentContext")

    if not context and context_before:
        context = context_before

    if context:
        switch_context(context_name=context, inventory_dir=inventory_dir)

    yield

    if context:
        if context_before:
            switch_context(context_name=context_before, inventory_dir=inventory_dir)
        else:
            switch_context(context_name=None, inventory_dir=inventory_dir)


def print_version() -> None:
    print(__version__)


def install_playbooks():
    parent_dir, req_file = os.path.split(ANSIBLE_REQUIREMENTS_FILE)

    subprocess.call(
        ["ansible-galaxy", "role", "install", "-r", req_file],
    )
    subprocess.call(
        ["ansible-galaxy", "collection", "install", "-r", req_file],
    )
    subprocess.call(
        [
            "ansible-galaxy",
            "collection",
            "install",
            "--force",
            os.path.join(parent_dir, "ansible_collections", "fresh2dev", "hostbutter"),
        ]
    )


def cluster(
    action: ClusterAction = yapx.arg(pos=True),
    command: Optional[str] = None,
    limit_to: str = "all",
):
    if action == ClusterAction.init:
        with chdir(os.path.dirname(os.environ["ANSIBLE_INVENTORY"])):
            subprocess.call(["ansible-playbook", "fresh2dev.hostbutter.apply_ssh"])
    elif action == ClusterAction.new:
        inventory: str = os.environ["ANSIBLE_INVENTORY"]
        if os.path.exists(inventory):
            raise FileExistsError(inventory)
        os.makedirs(os.path.dirname(inventory))
        with open(inventory, "w+", encoding="utf-8") as f:
            domain: str = os.getenv("DOMAIN", "example.com")
            f.write(
                f"""---
all:
  vars:
    domain: {domain}
    ansible_python_interpreter: python3
    ansible_port: 22
    ansible_ssh_private_key_file: "~/.ssh/id_ed25519.pub"
    root_ca_cert: ""
    timesync_timezone: America/Chicago
    fail2ban_install: true
    fail2ban_maxretry: 5     # allow up to 5 ssh failures,
    fail2ban_findtime: 1440  # in a 24-hour span,
    fail2ban_bantime: 10080  # ban for 7 days.
    dnsmasq_dns_servers:
      - 1.1.1.1
      - 1.0.0.1
    # dnsmasq_wildcard_addresses:
    #   "{domain}": "192.168.69.2"
    dnsmasq_host_records:
      "nas.{domain}": "192.168.69.2"
      "git.{domain}": "192.168.69.2"
      "registry.{domain}": "192.168.69.2"
    docker_daemon_options:
      dns: []
      default-address-pools:
        - base: "10.10.0.0/16"
          size: 24
      log-driver: "json-file"
      log-opts:
        max-size: "10m"
        max-file: "5"
      metrics-addr: '0.0.0.0:9323'
      experimental: true
  children:
    docker_swarm:
      children:
        docker_swarm_manager:
          hosts:
            swarm-mgr-01:
              ansible_host: "1.234.456.78"
              ansible_user: user
              docker_swarm_interface: enp7s0
              swarm_labels:
                - proxy
                - nas
                - frontend
                - backend
                - git-server
                - collector
              nfs_exports:
                - "/mnt/data            *(rw,fsid=0,crossmnt,sync,no_subtree_check,no_auth_nlm,insecure,no_root_squash)"
              firewall_additional_rules: []

        docker_swarm_worker:
          hosts: {{}}

    non_swarm: {{}}
"""
            )
        subprocess.call([os.getenv("EDITOR", "vim"), os.environ["ANSIBLE_INVENTORY"]])
    elif action == ClusterAction.edit:
        subprocess.call([os.getenv("EDITOR", "vim"), os.environ["ANSIBLE_INVENTORY"]])
    elif action == ClusterAction.ls:
        myke.echo.lines(os.listdir(os.environ["HOSTBUTTER_CONFIG_DIR"]))
    elif action == ClusterAction.nodes:
        subprocess.call(["ansible-inventory", "--graph"])
    elif action == ClusterAction.gather:
        subprocess.call(
            [
                "ansible",
                limit_to,
                "-m",
                "setup",
            ]
        )
    elif action == ClusterAction.ping:
        subprocess.call(
            [
                "ansible",
                limit_to,
                "-m",
                "ping",
            ]
        )
    elif action == ClusterAction.trust:
        with setenv(**{"ANSIBLE_HOST_KEY_CHECKING": "False"}):
            subprocess.call(
                [
                    "ansible",
                    limit_to,
                    "-m",
                    "ping",
                ]
            )
    elif action == ClusterAction.sh:
        subprocess.call(["ansible", limit_to, "-m", "shell", "-a", command])
    else:
        raise NotImplementedError()


def swarm(
    action: SwarmAction = yapx.arg(pos=True),
):
    if action == SwarmAction.ping:
        cluster(action=ClusterAction.ping, limit_to="docker_swarm")
    elif action == SwarmAction.prune:
        cluster(
            action=ClusterAction.sh,
            limit_to="docker_swarm",
            command='docker system prune --all --volumes --force && (for x in "volume"; do docker $x rm $(docker $x ls -q) 2>/dev/null || true; done)',
        )
    elif action == SwarmAction.stats:
        cluster(
            action=ClusterAction.sh,
            limit_to="docker_swarm",
            command="docker stats --no-stream",
        )
    elif action == SwarmAction.reboot:
        with chdir(os.path.dirname(os.environ["ANSIBLE_INVENTORY"])):
            subprocess.call(
                [
                    "ansible-playbook",
                    "-l",
                    "docker_swarm",
                    "fresh2dev.hostbutter.reboot_swarm",
                ]
            )
    elif action == SwarmAction.setup:
        with chdir(os.path.dirname(os.environ["ANSIBLE_INVENTORY"])):
            subprocess.call(
                [
                    "ansible-playbook",
                    "-l",
                    "docker_swarm",
                    "fresh2dev.hostbutter.apply_swarm",
                ]
            )
    else:
        raise NotImplementedError()


# TODO:
# def stack(up|down|config|ls|ll|rm|wait|new):
#     subprocess.call(["docker", "compose", "config"])
# def service(health|sh|restart|logs|down|config|ls|ll|rm|wait):
# def secrets(ls|push|pull):
# def image(ls|creds|pull|build|rm):
# def ci(ls|activate|deploy):
## THEN, retire .hostbutter.bashrc


def main() -> None:
    yapx.run(
        setup,
        cluster,
        swarm,
        install=install_playbooks,
        version=print_version,
        _args=sys.argv[1:],
    )


if __name__ == "__main__":
    main()
