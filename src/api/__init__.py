import fastapi

from . import game, note, systemic, user


router = fastapi.APIRouter(prefix='/v1')

router.include_router(game.router)
router.include_router(note.router)
router.include_router(systemic.router)
router.include_router(user.router)
