import datetime

import sqlalchemy
import sqlalchemy.orm as orm
import sqlalchemy.sql


class Base(orm.DeclarativeBase):
    pass


class ModelWithPK(Base):
    __abstract__ = True

    id_model: orm.Mapped[int] = orm.mapped_column(primary_key=True)


class NoteModel(ModelWithPK):
    __tablename__ = 'NoteModel'

    title: orm.Mapped[str]
    description: orm.Mapped[str]
    image: orm.Mapped[str]
    user_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('UserModel.id_model'),
    )
    user: orm.Mapped['UserModel'] = orm.relationship(
        'UserModel',
        back_populates='notes',
    )


class GameModel(ModelWithPK):
    __tablename__ = 'GameModel'

    score: orm.Mapped[int]
    game_date: orm.Mapped[datetime.datetime] = orm.mapped_column(
        sqlalchemy.DateTime,
        server_default=sqlalchemy.sql.func.now(),
    )
    user_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('UserModel.id_model'),
    )
    user: orm.Mapped['UserModel'] = orm.relationship(
        'UserModel',
        back_populates='games',
    )


class UserModel(ModelWithPK):
    __tablename__ = 'UserModel'

    ip: orm.Mapped[str] = orm.mapped_column(unique=True)
    games: orm.Mapped[list[GameModel] | None] = orm.relationship(
        back_populates='user',
    )
    notes: orm.Mapped[list[NoteModel] | None] = orm.relationship(
        back_populates='user',
    )
