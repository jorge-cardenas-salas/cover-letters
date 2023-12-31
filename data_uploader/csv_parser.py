import csv
from csv import DictReader
from logging import Logger
from typing import List, Optional, Tuple, Dict

from pydantic import ValidationError

from common.constants import FailMode
from common.models.user_model import UserModel
from common.utilities import DefaultLogger
from api.database.daos.dao import Dao


class CsvParser:
    EXPECTED_HEADERS = {"email", "name", "phone", "skillLevel", "skillName"}

    def __init__(self, logger: Optional[Logger] = None, fail_mode: FailMode = FailMode.BATCH, dao:Dao = None):
        # self.users: List[UserModel] = []
        # We'll use this to consolidate incoming data before parsing
        self.raw_data: Dict[str, dict] = {}
        self.invalid_data: list = []
        self.logger: Logger = logger or DefaultLogger().get_logger()
        self.fail_mode: FailMode = fail_mode
        self.success = True
        self.dao = dao or Dao()

    def upload(self, filename: str) -> bool:
        """
        Upload the selected file to the system (database)

        Args:
            filename: The file to upload
        Returns:
            bool: True if all records were successful, false otherwise
        """
        try:
            with open(filename, "r") as file:
                reader: DictReader = csv.DictReader(file)
                headers = set(reader.fieldnames)
                if headers != self.EXPECTED_HEADERS:
                    raise ValueError(f"Headers are incorrect, expected: {list(self.EXPECTED_HEADERS)}")

                for i, row in enumerate(reader):
                    valid, error = self.parse_row(i=i, row=row)
                    if not valid:
                        self.invalid_data.append({"row": i, "error": error, "raw_data": row})
                        self.success = False
                        self.logger.error(error)

            if self.fail_mode == FailMode.BATCH and not self.success:
                return self.success

            models = self.create_models()

            self.dao.merge_users(models)

        except Exception as ex:
            self.logger.error(str(ex))
            self.success = False

        return self.success

    def create_models(self) -> List[UserModel]:
        output: List[UserModel] = []
        for user in self.raw_data.values():
            try:
                # model = UserModel.model_validate(**user)
                model = UserModel(**user)
                output.append(model)
            except (ValidationError, TypeError) as ex:
                self.logger.error(f"Model error:{str(ex)}")
                self.success = False

        return output

    def parse_row(self, i: int, row: dict) -> Tuple[bool, str]:
        """
        Parse a single CSV row and add it to the raw data

        Args:
            i: The CSV row number for reference
            row: A dict representation of a CSV row
        Returns: Tuple:
            bool: True if success, false otherwise
            str: Error description, if applicable
        """
        if not row.get("email"):
            return False, f"Error in Row {i}: missing email"
        email: str = row.get("email")
        email = email.strip()
        if not email:
            return False, f"Error in Row {i}: missing email"

        # Retrieve user from our raw data (if it exists)
        user = self.raw_data.get(email)
        if not user:
            user = {
                "name": row.get("name"),
                "email": email,
                "phone": row.get("phone"),
                "skills": []
            }

        skill_level = row.get("skillLevel")
        if not skill_level:
            skill_level = 0

        try:
            skill_level = int(skill_level)
        except ValueError:
            return False, f"Error in Row {i}: skill level must be numeric"

        skill = {
            "name": row.get("skillName"),
            "level": skill_level
        }
        user["skills"].append(skill)
        self.raw_data[email] = user

        return True, ""

