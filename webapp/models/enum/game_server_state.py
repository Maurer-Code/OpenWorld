from enum import Enum


class GameServerState(Enum):
    STARTED = "STARTED"
    STOPPED = "STOPPED"
    REMOVED = "REMOVED"
    RUNNING = "RUNNING"
