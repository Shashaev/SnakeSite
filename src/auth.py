import datetime
import http
import typing

import bcrypt
import fastapi
import jwt

import src.db.dao
import src.db.models
import src.settings


encoding_for_hash: str = 'UTF-8'


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(
        password.encode(encoding_for_hash),
        salt,
    )


def check_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(
        password.encode(encoding_for_hash),
        hashed_password,
    )


def create_jwt_token(data: dict[str, typing.Any]) -> str:
    now_date = datetime.datetime.now(datetime.timezone.utc)
    data['iat'] = now_date
    data['exp'] = now_date + datetime.timedelta(days=src.settings.JWT_EXT_DAY)
    return jwt.encode(
        data,
        src.settings.SECRET_KEY,
        src.settings.ALGORITHM_FOR_HASH,
    )


def get_token(session_id: str | None = fastapi.Cookie(default=None)) -> str:
    jwt_token = session_id
    if not jwt_token:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
            detail='Пользователь не авторизован',
        )

    return jwt_token


def get_current_user(
    token: str = fastapi.Depends(get_token),
    user_dao: src.db.dao.UserDAO = fastapi.Depends(src.db.dao.get_userdao),
) -> src.db.models.UserModel | None:
    try:
        data = jwt.decode(
            token,
            src.settings.SECRET_KEY,
            algorithms=[src.settings.ALGORITHM_FOR_HASH],
        )
    except jwt.ExpiredSignatureError:
        raise fastapi.HTTPException(
            status_code=http.HTTPStatus.UNAUTHORIZED,
            detail='Токен истёк',
        )
    except Exception:
        raise fastapi.HTTPException(
            status_code=http.HTTPStatus.UNAUTHORIZED,
            detail='Токен не валиден',
        )

    return user_dao.select(data['user_id'])


def get_token_or_none(
    session_id: str | None = fastapi.Cookie(default=None),
) -> str | None:
    jwt_token = session_id
    if not jwt_token:
        return None

    return jwt_token


def get_current_user_or_none(
    token: str | None = fastapi.Depends(get_token_or_none),
    user_dao: src.db.dao.UserDAO = fastapi.Depends(src.db.dao.get_userdao),
) -> src.db.models.UserModel | None:
    if token is None:
        return None

    try:
        data = jwt.decode(
            token,
            src.settings.SECRET_KEY,
            algorithms=[src.settings.ALGORITHM_FOR_HASH],
        )
    except Exception:
        return None

    return user_dao.select(data['user_id'])
