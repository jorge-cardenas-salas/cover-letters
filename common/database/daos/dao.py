from typing import List

from sqlalchemy.orm import Session

from common.database.table_models.table_row_models import UserTableRow, SkillTableRow
from common.models.user_model import UserModel


class Dao:
    @staticmethod
    def merge_users(session: Session, user_models: List[UserModel]):
        # TODO: Make this an actual merge, for the sake of time, this just inserts
        row_models = Dao.create_models(user_models=user_models)
        session.add_all(row_models)
        session.commit()
        return row_models

    @staticmethod
    def create_models(user_models: List[UserModel]) -> List[UserTableRow]:
        output: List[UserTableRow] = []
        for user in user_models:
            skill_rows = []
            for skill in user.skills:
                skill_row = SkillTableRow(name=skill.name, level=skill.level.value)
                skill_rows.append(skill_row)
            user_row = UserTableRow(
                name=user.name, email=user.email, skills=skill_rows,
                id=user.id
            )
            output.append(user_row)

        return output
