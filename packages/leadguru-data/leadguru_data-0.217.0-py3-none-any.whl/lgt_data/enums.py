from enum import Enum, IntFlag


class DedicatedBotState(IntFlag):
    Operational = 0
    Stopped = 1
    ScheduledForDeletion = 2

class UserAccountState(IntFlag):
    Operational = 0
    Suspended = 1


class UserRole(str, Enum):
    ADMIN = 'admin'
    USER = 'user'
    MODERATOR = 'moderator'
