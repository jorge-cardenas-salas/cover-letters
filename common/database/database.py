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
Base = declarative_base()


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
    session = SessionLocal()
    try:
        # `yield` returns a generator for the session, aka an iterable that can only iterate once
        # In this case it returns a new Session every time is called, but forgets the previous sessions immediately
        yield session
    finally:
        session.close()
