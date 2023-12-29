import urllib.parse

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USE_LOCALHOST = True


def mysql_str() -> str:
    return "mysql://root:Answer2Life=42_Mysql@localhost:3306/coverletter"


def sqlite_str() -> str:
    return "sqlite:///./coverletter.db"


def pyodbc_url():
    connection_string = (
        r"Driver={ODBC Driver 18 for SQL Server};"
        r"Server=amaroq-sql-server.database.windows.net,1433;"
        r"Uid=rwuser;"
        r"Pwd=ColumbiaMd!2010;"
        r"Database=amaroqDb;"
        r"Encrypt=yes;"
        r"TrustServerCertificate=no;"
        r"Connection Timeout=30;"
    )
    connection_url = URL.create(
        "mssql+pyodbc",
        query={"odbc_connect": urllib.parse.quote_plus(connection_string)}
    )
    return connection_url


engine = create_engine(sqlite_str() if USE_LOCALHOST else pyodbc_url())
# Create our session class
# Each instance of the SessionLocal class will be a database session.
# We name it SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Now we will use the function declarative_base() that returns a class.
# Later we will inherit from this class to create each of the database models or classes (the ORM models)
# TODO: This seems like something that should be imported directly from the models ?
Base = declarative_base()
