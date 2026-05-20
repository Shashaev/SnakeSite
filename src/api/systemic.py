import fastapi

import src.schemes


router = fastapi.APIRouter(tags=['Systemic'])


@router.get('/ping')
def ping() -> src.schemes.StatusOk:
    """Healthcheck"""
    return src.schemes.StatusOk()
