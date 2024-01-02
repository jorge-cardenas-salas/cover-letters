from enum import Enum


class ExpertiseLevel(Enum):
    BEGINNER = 0
    INTERMEDIATE = 1
    ADVANCED = 2
    EXPERT = 3


class FailMode(Enum):
    BATCH = 0
    ROW = 1


PROJECT_NAME = "cover-letter-api"

DEFAULT_LOG_FORMAT = "%(name)s | %(asctime)s | %(levelname)s | %(module)s.%(processName)s: %(message)s"
