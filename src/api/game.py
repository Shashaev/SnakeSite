import fastapi

import src.auth
import src.db.dao
import src.db.models
import src.schemes


router = fastapi.APIRouter(prefix='/game', tags=['Games'])


@router.post('/add')
async def add_note(
    score: int = fastapi.Form(...),
    user: src.db.models.UserModel | None = fastapi.Depends(
        src.auth.get_current_user,
    ),
    game_dao: src.db.dao.GameDAO = fastapi.Depends(src.db.dao.get_gamedao),
) -> src.schemes.StatusOk:
    game = src.db.models.GameModel(
        score=score,
        user=user,
    )
    game_dao.create(game)
    return src.schemes.StatusOk()
