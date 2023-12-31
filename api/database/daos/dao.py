from sqlalchemy.orm import Session

from api.database.table_models.table_row_models import UserTableRow, SkillTableRow
from common.models.user_model import UserModel
from typing import List

class Dao:
    @staticmethod
    def create_user(session: Session, user_model: UserModel) -> UserTableRow:
        # Create the row model from the user model
        skill_rows = []
        for skill in user_model.skills:
            skill_row = SkillTableRow(name=skill.name, level=skill.level.value)
            skill_rows.append(skill_row)

        user_row = UserTableRow(
            name=user_model.name, email=user_model.email, skills=skill_rows,
            id=user_model.id
        )
        session.add(user_row)
        session.commit()

        # I presume I would be updating the data (mostly the PK) from the DB
        session.refresh(user_row)
        return user_row

    def merge_users(session: Session, user_models: List[UserModel]):
        pass
        # with session.connection() as conn:
        #     conn.execute("-- MERGE statement goes here")
        #
        # return session.commit()
