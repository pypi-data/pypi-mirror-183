import os
from contextlib import contextmanager
from typing import Optional


@contextmanager
def chdir(path: str):
    path_og = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(path_og)


@contextmanager
def setenv(**kwargs):
    env_og = os.environ.copy()
    try:
        os.environ.update(kwargs)
        yield
    finally:
        os.environ = env_og


def switch_context(context_name: Optional[str], inventory_dir: str):
    if context_name is None:
        del os.environ["DOCKER_CONTEXT"]
        del os.environ["ANSIBLE_INVENTORY"]
        del os.environ["DOMAIN"]
        del os.environ["IMAGE_REGISTRY"]
        del os.environ["NFS_OPTS"]
    else:
        os.environ["DOCKER_CONTEXT"] = context_name
        os.environ["ANSIBLE_INVENTORY"] = os.path.join(
            inventory_dir, os.environ["DOCKER_CONTEXT"], "inventory.yml"
        )
        os.environ["DOMAIN"] = os.environ["DOCKER_CONTEXT"]
        os.environ["IMAGE_REGISTRY"] = f"registry.{os.environ['DOCKER_CONTEXT']}"
        os.environ["NFS_OPTS"] = f"addr=nas.{os.environ['DOMAIN']},vers=4.1,rw"
