from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from common.database.daos.dao import Dao
from common.database.database import get_session
from common.models.user_model import UserModel
from common.utilities import DefaultLogger
from data_uploader.csv_parser import CsvParser

app = FastAPI()

logger = DefaultLogger(use_file=True).get_logger()


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


@app.get("/upload-file")
def upload_file(filename: str):
    result = False
    try:
        parser = CsvParser()
        result = parser.upload(filename=filename)
    except Exception as ex:
        logger.exception(str(ex))

    return f"Success: {result}"


@app.post("/retrieve-users")
def retrieve_users(ids: List[int], session: Session = Depends(get_session)):
    try:
        output = Dao.select_users(ids=ids, session=session)
        return output
    except Exception as ex:
        logger.exception(str(ex))


@app.delete("/delete-users")
def delete_users(ids: List[int], session: Session = Depends(get_session)):
    try:
        Dao.delete_users(ids=ids, session=session)
        return {"success": True}
    except Exception as ex:
        logger.exception(str(ex))
        return {"success": False}


@app.patch("/update-user")
def update_user(user_id: int, model: UserModel, session: Session = Depends(get_session)):
    try:
        Dao.update_user(user_id=user_id, session=session, user_model=model)
        return {"success": True}
    except Exception as ex:
        logger.exception(str(ex))
        return {"success": False}
