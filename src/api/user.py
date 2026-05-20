import http

import fastapi

import src.auth
import src.db.dao
import src.db.models
import src.schemes
import src.settings


router = fastapi.APIRouter(prefix='/user', tags=['Users'])


@router.post('/registration')
def registration(
    data: src.schemes.UserData,
    user_dao: src.db.dao.UserDAO = fastapi.Depends(src.db.dao.get_userdao),
) -> src.schemes.StatusOk:
    user = user_dao.select_by_user_name(data.username)
    if user is not None:
        raise fastapi.HTTPException(
            http.HTTPStatus.CONFLICT,
            detail='Пользователь с тамим именем уже существует',
        )

    password = src.auth.hash_password(data.password)
    user_dao.create(src.db.models.UserModel(
        name=data.username,
        password=password,
    ))
    print(password)
    return src.schemes.StatusOk()


@router.post('/authentication')
def authentication(
    response: fastapi.Response,
    data: src.schemes.UserData,
    user_dao: src.db.dao.UserDAO = fastapi.Depends(src.db.dao.get_userdao),
) -> src.schemes.StatusOk:
    user = user_dao.select_by_user_name(data.username)
    if (
        user is None
        or not src.auth.check_password(data.password, user.password)
    ):
        raise fastapi.HTTPException(
            http.HTTPStatus.UNAUTHORIZED,
            detail='Неверное имя пользователя или пароль',
        )

    jwt_token = src.auth.create_jwt_token({'user_id': user.id_model})
    response.set_cookie(
        'session_id',
        jwt_token,
        src.settings.JWT_EXT_SECONDS,
        httponly=True,
    )
    return src.schemes.StatusOk()
