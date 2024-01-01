import re
from typing import List, Optional

from pydantic import BaseModel, EmailStr, field_validator

from common.models.skill_model import SkillModel


class UserModel(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    skills: Optional[List[SkillModel]] = []
    phone: str

    @field_validator("phone")
    @classmethod # this goes AFTER field_validator, regardless what PyCharm says >:-(
    def validate_phone(cls, value: str):
        pattern = "^(\\+\\d+)?(\\(\\d+\\))?\\s*[\\d-]+$"
        # Even though we use assert, this should throw a ValidationError
        assert re.match(pattern=pattern, string=value), "Phone doesn't match expected pattern"
        return value

    @field_validator("name")
    @classmethod
    def validate_alphanums(cls, value: str) -> str:
        pattern = "^[a-zA-Z\\s]+"
        assert re.match(pattern=pattern, string=value), "Phone doesn't match expected pattern"
        return value

    # Now, in the Pydantic models, add an internal Config class.
    # This Config class is used to provide configurations to Pydantic.
    # In the Config class, set the attribute orm_mode = True.
    class Config:
        orm_mode = True
