import fastapi
import sqlalchemy
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
    model = models.GameModel


class UserDAO(BaseDAO):
    model = models.UserModel

    def select_by_user_ip(self, user_ip: str) -> models.UserModel | None:
        return (
            self.session
            .query(self.model)
            .filter_by(ip=user_ip)
            .first()
        )


class NoOrmNoteDao:
    def __init__(self, session: orm.Session):
        self.connection = session.connection()

    def create(self, note: models.NoteModel) -> None:
        stmt = sqlalchemy.text("""
            INSERT INTO "NoteModel" (title, description, image, user_id)
            VALUES (:title, :description, :image, :user_id)
        """)
        self.connection.execute(
            stmt,
            {
                'title': note.title,
                'description': note.description,
                'image': note.image,
                'user_id': note.user_id
            }
        )
        self.connection.commit()

    def select(self, pk: int) -> models.NoteModel | None:
        stmt = sqlalchemy.text("""
            SELECT id_model, title, description, image, user_id
            FROM "NoteModel"
            WHERE id_model = :pk
        """)
        row = self.connection.execute(stmt, {'pk': pk}).fetchone()
        if row is None:
            return None

        return models.NoteModel(
            id_model=row.id_model,
            title=row.title,
            description=row.description,
            image=row.image,
            user_id=row.user_id
        )

    def select_all(self) -> list[models.NoteModel]:
        stmt = sqlalchemy.text("""
            SELECT id_model, title, description, image, user_id
            FROM "NoteModel"
        """)
        rows = self.connection.execute(stmt).fetchall()
        return [
            models.NoteModel(
                id_model=row.id_model,
                title=row.title,
                description=row.description,
                image=row.image,
                user_id=row.user_id
            )
            for row in rows
        ]

    def update(self, note: models.NoteModel) -> None:
        stmt = sqlalchemy.text("""
            UPDATE "NoteModel"
            SET title = :title,
                description = :description,
                image = :image,
                user_id = :user_id
            WHERE id_model = :id_model
        """)
        self.connection.execute(
            stmt,
            {
                'id_model': note.id_model,
                'title': note.title,
                'description': note.description,
                'image': note.image,
                'user_id': note.user_id
            }
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        stmt = sqlalchemy.text('DELETE FROM "NoteModel" WHERE id_model = :pk')
        self.connection.execute(stmt, {"pk": pk})
        self.connection.commit()

    def delete_all(self) -> None:
        stmt = sqlalchemy.text('DELETE FROM "NoteModel"')
        self.connection.execute(stmt)
        self.connection.commit()


class NoOrmGameDao:
    def __init__(self, session: orm.Session):
        self.connection = session.connection()

    def create(self, game: models.GameModel) -> None:
        stmt = sqlalchemy.text("""
            INSERT INTO "GameModel" (score, game_date, user_id)
            VALUES (:score, :game_date, :user_id)
        """)
        self.connection.execute(
            stmt,
            {
                'score': game.score,
                'game_date': game.game_date,
                'user_id': game.user_id
            }
        )
        self.connection.commit()

    def select(self, pk: int) -> models.GameModel | None:
        stmt = sqlalchemy.text("""
            SELECT id_model, score, game_date, user_id
            FROM "GameModel"
            WHERE id_model = :pk
        """)
        row = self.connection.execute(stmt, {'pk': pk}).fetchone()
        if row is None:
            return None

        return models.GameModel(
            id_model=row.id_model,
            score=row.score,
            game_date=row.game_date,
            user_id=row.user_id
        )

    def select_all(self) -> list[models.GameModel]:
        stmt = sqlalchemy.text("""
            SELECT id_model, score, game_date, user_id
            FROM "GameModel"
        """)
        rows = self.connection.execute(stmt).fetchall()
        return [
            models.GameModel(
                id_model=row.id_model,
                score=row.score,
                game_date=row.game_date,
                user_id=row.user_id
            )
            for row in rows
        ]

    def update(self, game: models.GameModel) -> None:
        stmt = sqlalchemy.text("""
            UPDATE "GameModel"
            SET score = :score,
                game_date = :game_date,
                user_id = :user_id
            WHERE id_model = :id_model
        """)
        self.connection.execute(
            stmt,
            {
                'id_model': game.id_model,
                'score': game.score,
                'game_date': game.game_date,
                'user_id': game.user_id
            }
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        stmt = sqlalchemy.text('DELETE FROM "GameModel" WHERE id_model = :pk')
        self.connection.execute(stmt, {'pk': pk})
        self.connection.commit()

    def delete_all(self) -> None:
        stmt = sqlalchemy.text('DELETE FROM "GameModel"')
        self.connection.execute(stmt)
        self.connection.commit()


class NoOrmUserDao:
    def __init__(self, session: orm.Session):
        self.connection = session.connection()

    def create(self, user: models.UserModel) -> None:
        stmt = sqlalchemy.text("""
            INSERT INTO "UserModel" (ip)
            VALUES (:ip)
        """)
        self.connection.execute(stmt, {'ip': user.ip})
        self.connection.commit()

    def select(self, pk: int) -> models.UserModel | None:
        stmt = sqlalchemy.text("""
            SELECT id_model, ip
            FROM "UserModel"
            WHERE id_model = :pk
        """)
        row = self.connection.execute(stmt, {'pk': pk}).fetchone()
        if row is None:
            return None

        return models.UserModel(id_model=row.id_model, ip=row.ip)

    def select_all(self) -> list[models.UserModel]:
        stmt = sqlalchemy.text('SELECT id_model, ip FROM "UserModel"')
        rows = self.connection.execute(stmt).fetchall()
        return [
            models.UserModel(id_model=row.id_model, ip=row.ip)
            for row in rows
        ]

    def update(self, user: models.UserModel) -> None:
        stmt = sqlalchemy.text("""
            UPDATE "UserModel"
            SET ip = :ip
            WHERE id_model = :id_model
        """)
        self.connection.execute(
            stmt,
            {'id_model': user.id_model, 'ip': user.ip},
        )
        self.connection.commit()

    def delete(self, pk: int) -> None:
        stmt = sqlalchemy.text('DELETE FROM "UserModel" WHERE id_model = :pk')
        self.connection.execute(stmt, {'pk': pk})
        self.connection.commit()

    def delete_all(self) -> None:
        stmt = sqlalchemy.text('DELETE FROM "UserModel"')
        self.connection.execute(stmt)
        self.connection.commit()

    def select_by_user_ip(self, user_ip: str) -> models.UserModel | None:
        stmt = sqlalchemy.text("""
            SELECT id_model, ip
            FROM "UserModel"
            WHERE ip = :user_ip
        """)
        row = self.connection.execute(stmt, {'user_ip': user_ip}).fetchone()
        if row is None:
            return None

        return models.UserModel(id_model=row.id_model, ip=row.ip)


def get_notedao(
    session: orm.Session = fastapi.Depends(db.get_db),
) -> NoOrmNoteDao:
    return NoOrmNoteDao(session)


def get_gamedao(
    session: orm.Session = fastapi.Depends(db.get_db),
) -> NoOrmGameDao:
    return NoOrmGameDao(session)


def get_userdao(
    session: orm.Session = fastapi.Depends(db.get_db),
) -> NoOrmUserDao:
    return NoOrmUserDao(session)
