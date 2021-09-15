from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Base

from ..config import Config

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    isolation_level='READ UNCOMMITTED',
)


def create_database():
    Base.metadata.create_all(bind=engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine, expire_on_commit=False)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
