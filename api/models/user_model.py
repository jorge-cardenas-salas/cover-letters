from typing import List

from pydantic import BaseModel

from api.models.skill_model import SkillModel


class UserModel(BaseModel):
    name: str
    email: str
    skills: List[SkillModel]
