import fastapi
import sqlalchemy.orm as orm

import src.db.db as db
import src.db.models as models


class BaseDAO[T: models.Base]:
    model: type[T]

    def __init__(self, session: orm.Session) -> None:
        self.session = session

    def create(self, model: T) -> None:
        self.session.add(model)
        self.session.commit()

    def select(self, pk: int) -> T | None:
        return self.session.get(self.model, pk)

    def select_all(self) -> list[T]:
        return self.session.query(self.model).all()

    def update(self, model: T) -> None:
        self.session.add(model)
        self.session.commit()

    def delete(self, pk: int) -> None:
        self.session.delete(self.select(pk))
        self.session.commit()

    def delete_all(self) -> None:
        self.session.query(self.model).delete()
        self.session.commit()


class NoteDAO(BaseDAO):
    model: type[models.NoteModel] = models.NoteModel


class GameDAO(BaseDAO):
    model: type[models.GameModel] = models.GameModel


class UserDAO(BaseDAO):
    model: type[models.UserModel] = models.UserModel

    def select_by_user_name(self, username: str) -> models.UserModel | None:
        return (
            self.session
            .query(self.model)
            .filter_by(name=username)
            .first()
        )


def get_notedao(
    session: orm.Session = fastapi.Depends(db.get_db),
) -> NoteDAO:
    return NoteDAO(session)


def get_gamedao(
    session: orm.Session = fastapi.Depends(db.get_db),
) -> GameDAO:
    return GameDAO(session)


def get_userdao(
    session: orm.Session = fastapi.Depends(db.get_db),
) -> UserDAO:
    return UserDAO(session)
