from sqlalchemy import create_engine
from sqlalchemy.ext.declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./db/sql_lite.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connnect_args={"check_same_thread": False}
)  # "check_same_thread": False only for sqlite db
SessionLocal = sessionmaker(autocommit=False, autoflush=Falsse, bind=engine)

Base = declarative_base()