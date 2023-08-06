from enum import Enum, auto


class ClusterAction(Enum):
    ls = auto()
    new = auto()
    nodes = auto()
    edit = auto()
    setup = auto()
    gather = auto()
    ping = auto()
    trust = auto()
    init = auto()
    sh = auto()


class SwarmAction(Enum):
    setup = auto()
    ping = auto()
    prune = auto()
    stats = auto()
    reboot = auto()


class StackAction(Enum):
    ls = auto()
    up = auto()
    down = auto()
    config = auto()
    rm = auto()
    wait = auto()
    new = auto()


class ServiceAction(Enum):
    ls = auto()
    sh = auto()
    logs = auto()
    rm = auto()


class SecretAction(Enum):
    ls = auto()
    push = auto()
    pull = auto()


class ImageAction(Enum):
    ls = auto()
    rm = auto()
    pull = auto()
    build = auto()


class CiAction(Enum):
    ls = auto()
    activate = auto()
    deploy = auto()
