import os
import typing

import dotenv


dotenv.load_dotenv()


def is_bool(string: str) -> bool:
    string = string.lower()
    return (
        string == 'true'
        or string == 't'
    )


USE_POSTGRESQL: typing.Final = is_bool(os.getenv(
    'API_USE_POSTGRESQL',
    'False',
))

# PostgreSQL settings
DB_USER: typing.Final = os.getenv('API_DB_USER', 'postgres')
DB_PASSWORD: typing.Final = os.getenv('API_DB_PASSWORD', 'example')
DB_HOST: typing.Final = 'db'
DB_PORT: typing.Final = '5432'
DB_NAME: typing.Final = os.getenv('API_DB_NAME', 'snakesite')

# SQLite settings
PATH_DB: typing.Final = os.getenv('API_DB_PATH', 'database.db')

CONNECTION_STRING: typing.Final = (
    f'postgresql+asyncpg://{DB_USER}:'
    f'{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
) if USE_POSTGRESQL else f'sqlite:///{PATH_DB}'

USE_MOCK_DATA: typing.Final = is_bool(os.getenv('API_USE_MOCK_DATA', 'True'))

SECRET_KEY: typing.Final = os.getenv('API_JWT_SECRET_KEY', 'example')
ALGORITHM_FOR_HASH: typing.Final = 'HS256'
JWT_EXT_DAY: typing.Final = int(os.getenv('API_JWT_EXT_DAY', '30'))
JWT_EXT_SECONDS: typing.Final = JWT_EXT_DAY * 24 * 60 * 60

DEBUG: typing.Final = is_bool(os.getenv('DEBUG', 'True'))

UPLOAD_DIR: typing.Final = 'src/uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

UPLOAD_PREFIX: typing.Final = '/uploads'
