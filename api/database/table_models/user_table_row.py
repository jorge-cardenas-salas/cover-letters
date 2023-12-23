from api.database.database import Base
from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship


class UserTableRow(Base):
    __tablename__ = "tblUser"

    """
    SQLAlchemy ORM (Object Relational Model) representation of the table
    """
    id = Column(BigInteger, primary_key=True, unique=True, index=True)
    userName = Column(String, unique=True, index=False)
    email = Column(String, unique=True, index=False)

    # TODO: Add relationships here, to link skills to users and other tables
    # https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_1_3
    skills = relationship("SkillTable", back_populates="user")
