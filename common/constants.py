from enum import Enum


class ExpertiseLevel(Enum):
    BEGINNER = 0
    INTERMEDIATE = 1
    ADVANCED = 2
    EXPERT = 3


PROJECT_NAME = "cover-letter-api"

DEFAULT_LOG_FORMAT = "%(name)s | %(asctime)s | %(levelname)s | %(module)s.%(processName)s: %(message)s"
