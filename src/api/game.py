import collections

import fastapi

import src.auth
import src.db.dao
import src.db.models
import src.schemes


router = fastapi.APIRouter(prefix='/game', tags=['Games'])


@router.post('/add')
async def add_game(
    score: int = fastapi.Form(...),
    user: src.db.models.UserModel = fastapi.Depends(
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


@router.get('/leaderboard')
async def get_leaderboard(
    game_dao: src.db.dao.GameDAO = fastapi.Depends(src.db.dao.get_gamedao),
    user_dao: src.db.dao.UserDAO = fastapi.Depends(src.db.dao.get_userdao),
) -> list[src.schemes.LeaderboardLine]:
    games = game_dao.select_all()
    user_to_maxscore: dict[int, int] = collections.defaultdict(int)
    for game in games:
        user_to_maxscore[game.user_id] = max(
            user_to_maxscore[game.user_id],
            game.score,
        )

    return [
        src.schemes.LeaderboardLine(
            username=(
                user.name
                if (user := user_dao.select(user_id))
                else 'Anonymous'
            ),
            maxscore=maxscore,
        )
        for user_id, maxscore in sorted(
            user_to_maxscore.items(),
            key=lambda x: x[1],
            reverse=True,
        )
    ]
