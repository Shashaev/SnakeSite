import typing

import fastapi
import fastapi.responses
import fastapi.templating

import src.db.dao
import src.db.models


router = fastapi.APIRouter()
templates = fastapi.templating.Jinja2Templates(directory='src/templates')


@router.get('/ping')
def ping() -> dict[
    typing.Literal['status'],
    typing.Literal['ok'],
]:
    """Healthcheck"""
    return {'status': 'ok'}


@router.get('/game')
def game(request: fastapi.Request) -> fastapi.responses.HTMLResponse:
    return templates.TemplateResponse(
        request,
        'game.html',
    )


@router.get('/feedback')
def feedback(request: fastapi.Request) -> fastapi.responses.HTMLResponse:
    return templates.TemplateResponse(
        request,
        'feedback.html',
    )


@router.get('/')
def index(request: fastapi.Request) -> fastapi.responses.HTMLResponse:
    return templates.TemplateResponse(
        request,
        'index.html',
    )


@router.get('/list_type_snakes')
def list_type_snakes(
    request: fastapi.Request,
    note_dao: src.db.dao.NoteDAO = fastapi.Depends(src.db.dao.get_notedao),
) -> fastapi.responses.HTMLResponse:
    all_notes: list[src.db.models.NoteModel] = note_dao.select_all()
    return templates.TemplateResponse(
        request,
        'list_type_snakes.html',
        {'notes': all_notes},
    )


def _get_or_create_user_by_user_ip(
    user_ip: str,
    user_dao: src.db.dao.UserDAO = fastapi.Depends(src.db.dao.get_userdao),
) -> src.db.models.UserModel:
    user = user_dao.select_by_user_ip(user_ip)
    if user is None:
        user = src.db.models.UserModel(ip=user_ip)
        user_dao.create(user)

    return user


@router.post('/game/add')
def add_game(
    request: fastapi.Request,
    score: int,
    game_dao: src.db.dao.GameDAO = fastapi.Depends(src.db.dao.get_gamedao),
) -> None:
    user = _get_or_create_user_by_user_ip(request.client.host)
    game = src.db.models.GameModel(
        score=score,
        user=user,
    )
    game_dao.create(game)


@router.post('/add_note')
async def add_note(
    # request: fastapi.Request,
    title: str = fastapi.Form(...),
    description: str = fastapi.Form(...),
    image: str = fastapi.Form(...),
    note_dao: src.db.dao.NoteDAO = fastapi.Depends(src.db.dao.get_notedao),
):
    new_note = src.db.models.NoteModel(
        title=title,
        description=description,
        image=image,
        user_id=1,
    )
    note_dao.create(new_note)
    return fastapi.responses.RedirectResponse(
        url='/list_type_snakes',
        status_code=303,
    )


# @router.post('/note/add')
# def add_note(
#     user_ip: str,
#     title: str,
#     description: str,
#     image: str,
#     note_dao: src.db.dao.NoteDAO = fastapi.Depends(src.db.dao.get_notedao),
# ) -> None:
#     user = _get_or_create_user_by_user_ip(user_ip)
#     note = src.db.models.NoteModel(
#         title=title,
#         description=description,
#         image=image,
#         user=user,
#     )
#     note_dao.create(note)
