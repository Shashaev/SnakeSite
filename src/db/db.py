import typing

import sqlalchemy
import sqlalchemy.orm as orm

import src.db.models
import src.settings


engin = sqlalchemy.create_engine(src.settings.CONNECTION_STRING)


def create_db_and_tables():
    src.db.models.Base.metadata.create_all(engin)


def drop_db():
    src.db.models.Base.metadata.drop_all(engin)


sessionmaker = orm.sessionmaker(engin)


def get_db() -> typing.Generator[
    orm.Session,
    None,
    None,
]:
    with sessionmaker() as session:
        yield session
