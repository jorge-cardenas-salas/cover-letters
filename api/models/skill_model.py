from typing import Optional

from pydantic import BaseModel

from api.constants import ExpertiseLevel


class SkillModel(BaseModel):
    name: str
    level: Optional[ExpertiseLevel]