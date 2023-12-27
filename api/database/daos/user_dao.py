from sqlalchemy.orm import Session

from api.database.table_models.user_table_row import UserTableRow
from api.models.user_model import UserModel


class UserDao:
    @staticmethod
    def create_user(session: Session, user_model: UserModel) -> UserTableRow:
        # Create the row model from the user model
        user_row = UserTableRow(name=user_model.name, email=user_model.email, id=user_model.id)
        session.add(user_row)
        session.commit()

        # I presume I would be updating the data (mostly the PK) from the DB
        session.refresh(user_row)
        return user_row

    # TODO: Add create skills here? or in its own class?
