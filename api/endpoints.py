from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from common.database.daos.dao import Dao
from common.database.database import SessionLocal
from common.models.user_model import UserModel
from common.utilities import DefaultLogger

app = FastAPI()

logger = DefaultLogger(use_file=True).get_logger()


def get_session() -> SessionLocal:
    """
    We use the SessionLocal class to create a dependency. We need to have an independent database session/connection
    (SessionLocal) per request, use the same session through all the request and then close it after the request
    is finished.

    And then a new session will be created for the next request.

    For that, we will create a new dependency with yield. Our dependency will create a new SQLAlchemy SessionLocal
    that will be used in a single request, and then close it once the request is finished.

    Returns:
        SessionLocal: A DB session to be used once
    """
    # fetch session
    logger.info("Regular get_session")
    session = SessionLocal()
    try:
        # `yield` returns a generator for the session, aka an iterable that can only iterate once
        # In this case it returns a new Session every time is called, but forgets the previous sessions immediately
        yield session
    finally:
        session.close()


@app.put("/add-users")
def add_users(models: List[UserModel], session: Session = Depends(get_session)):
    """
    Create new users in the Database

    Args:
        models (UserModel): The user data to be added
        session (Session): The DB session to be used to store the data
    """
    # logger = get_local_logger()
    logger.info("Adding new user")
    try:
        new_users = Dao.merge_users(session=session, user_models=models)
        new_ids = [user.id for user in new_users]
        logger.info(f"New users created, id's: {new_ids}")
        return new_ids
    except Exception as ex:
        logger.exception(str(ex))
