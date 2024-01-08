from typing import List

import sqlalchemy
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

    @staticmethod
    def select_users(session: Session, ids: List[int]):
        if not ids:
            raise ValueError("At least an id is necessary")

        users = session.query(
            UserTableRow.id, UserTableRow.name  # , UserTableRow.skills
        ).filter(UserTableRow.id.in_(ids)).distinct()
        output = [{user.id, user.name} for user in users]

        return output

    @staticmethod
    def delete_users(session: Session, ids: List[int]):
        if not ids:
            raise ValueError("At least an id is necessary")

        users = session.query(
            UserTableRow
        ).filter(UserTableRow.id.in_(ids))
        try:
            for user in users:
                session.delete(user)
        except Exception as ex:
            session.rollback()
            raise ex

        session.commit()

    @staticmethod
    def update_user(user_id: int, user_model: UserModel, session: Session):
        try:
            session.execute(
                sqlalchemy.update(UserTableRow)
                .where(UserTableRow.id == user_id)
                .values(name=user_model.name)
            )
        except Exception as ex:
            session.rollback()
            raise ex

        session.commit()
