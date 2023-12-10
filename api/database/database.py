from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = "jdbc:mysql://jorge:Answer2Life=42_Mysql@localhost:3306/coverletter"
SQLALCHEMY_DATABASE_URL = "mysql://root:Answer2Life=42_Mysql@localhost:3306/coverletter"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create our session class
# Each instance of the SessionLocal class will be a database session.
# We name it SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Now we will use the function declarative_base() that returns a class.
# Later we will inherit from this class to create each of the database models or classes (the ORM models)
# TODO: This seems like something that should be imported directly from the models ?
Base = declarative_base()


