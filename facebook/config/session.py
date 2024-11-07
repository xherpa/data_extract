from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from facebook.config.config import URL_DATABASE

# Create engine to database
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
