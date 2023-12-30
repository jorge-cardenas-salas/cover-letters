from typing import Optional

from pydantic import BaseModel

from api.constants import ExpertiseLevel


class SkillModel(BaseModel):
    name: str
    level: Optional[ExpertiseLevel]
    user_id: Optional[int] = None

    class Config:
        orm_mode = True
