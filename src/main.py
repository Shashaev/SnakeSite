import contextlib
import typing

import fastapi
import fastapi.staticfiles
import uvicorn

import src.api
import src.core
import src.db.db
import src.settings


@contextlib.asynccontextmanager
async def lifespan(
    app: fastapi.FastAPI,
) -> typing.AsyncGenerator[
    None,
    None,
]:
    src.db.db.create_db_and_tables()
    if src.settings.USE_MOCK_DATA:
        src.core.mock_data()

    yield


app = fastapi.FastAPI(
    title='Snake Site',
    version='1.0',
    lifespan=lifespan,
)

app.include_router(src.api.router)
app.mount(
    '/src/static',
    fastapi.staticfiles.StaticFiles(directory='src/static'),
    name='static',
)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
    )
