from contextlib import contextmanager

from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.settings import Settings

# dialect+driver://username:password@host:port/database
DATABASE_URL = "mysql+{driver}://{user}:{password}@{host}:{port}/{database}".format(
    driver="mysqlconnector",
    user=Settings.mysql_username,
    host=Settings.mysql_host,
    port=Settings.mysql_port,
    password=Settings.mysql_password.get_secret_value(),
    database=Settings.mysql_database,
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def db_model_as_dict(obj):
    return {
        c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs
    }


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
