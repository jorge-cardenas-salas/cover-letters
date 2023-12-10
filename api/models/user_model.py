from typing import List, Optional

from pydantic import BaseModel

from api.models.skill_model import SkillModel


class UserModel(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    skills: List[SkillModel]

    # Now, in the Pydantic models, add an internal Config class.
    # This Config class is used to provide configurations to Pydantic.
    # In the Config class, set the attribute orm_mode = True.
    class Config:
        orm_mode = True
