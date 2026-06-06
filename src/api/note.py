import http

import fastapi

import src.auth
import src.db.dao
import src.db.models
import src.schemes
import src.settings


router = fastapi.APIRouter(prefix='/note', tags=['Notes'])


@router.get('/get_all')
def list_type_snakes(
    user: src.db.models.UserModel | None = fastapi.Depends(
        src.auth.get_current_user_or_none,
    ),
    note_dao: src.db.dao.NoteDAO = fastapi.Depends(src.db.dao.get_notedao),
) -> list[src.schemes.Note]:
    notes: list[src.db.models.NoteModel] = note_dao.select_all()
    return [
        src.schemes.Note(
            id_model=note.id_model,
            title=note.title,
            description=note.description,
            image=f'{src.settings.UPLOAD_PREFIX}/{note.image}',
            is_user=(
                user is not None
                and note.user_id == user.id_model
            ),
        )
        for note in notes
    ]


@router.post('/add')
def add(
    image: fastapi.UploadFile,
    title: str = fastapi.Form(...),
    description: str = fastapi.Form(...),
    user: src.db.models.UserModel = fastapi.Depends(
        src.auth.get_current_user,
    ),
    note_dao: src.db.dao.NoteDAO = fastapi.Depends(src.db.dao.get_notedao),
) -> src.schemes.StatusOk:
    path_to_file = f'{src.settings.UPLOAD_DIR}/{image.filename}'
    with open(path_to_file, 'wb') as file:
        file.write(image.file.read())

    new_note = src.db.models.NoteModel(
        title=title,
        description=description,
        image=image.filename,
        user_id=user.id_model,
    )
    note_dao.create(new_note)
    return src.schemes.StatusOk()


@router.post('/delete')
def delete(
    id_note: int = fastapi.Form(...),
    user: src.db.models.UserModel = fastapi.Depends(
        src.auth.get_current_user,
    ),
    note_dao: src.db.dao.NoteDAO = fastapi.Depends(src.db.dao.get_notedao),
) -> src.schemes.StatusOk:
    note = note_dao.select(id_note)
    if note is None:
        raise fastapi.HTTPException(
            http.HTTPStatus.CONFLICT,
            detail='Указанной статьи не найдено',
        )
    elif note.user_id != user.id_model:
        raise fastapi.HTTPException(
            http.HTTPStatus.FORBIDDEN,
            detail='Недостаточно прав',
        )

    note_dao.delete(id_note)
    return src.schemes.StatusOk()
