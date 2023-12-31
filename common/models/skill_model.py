from typing import Optional
import re
from pydantic import BaseModel, field_validator

from common.constants import ExpertiseLevel


class SkillModel(BaseModel):
    name: str
    level: Optional[ExpertiseLevel]
    user_id: Optional[int] = None

    class Config:
        orm_mode = True

    @classmethod
    @field_validator("name")
    def validate_phone(cls, value: str):
        pattern = "^[a-zA-Z\\s]+"
        assert re.match(pattern=pattern, string=value), "Phone doesn't match expected pattern"
        return value
