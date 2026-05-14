import os

import dotenv


dotenv.load_dotenv()


def is_bool(string: str) -> bool:
    string = string.lower()
    return (
        string == 'true'
        or string == 't'
    )


USE_POSTGRESQL = is_bool(os.getenv('API_USE_POSTGRESQL', 'False'))

PATH_DB = os.getenv('API_DB_PATH', 'database.db')
DB_USER = os.getenv('API_DB_USER', 'postgres')
DB_PASSWORD = os.getenv('API_DB_PASSWORD', 'example')
# DB_HOST = os.getenv('API_DB_HOST', 'db')
DB_HOST = 'db'
# DB_PORT = os.getenv('API_DB_PORT', '5432')
DB_PORT = '5432'
DB_NAME = os.getenv('API_DB_NAME', 'snakesite')

if not USE_POSTGRESQL:
    PATH_DB = 'database.db'
    CONNECTION_STRING = f'sqlite:///{PATH_DB}'
else:
    CONNECTION_STRING = (
        f'postgresql+asyncpg://{DB_USER}:'
        f'{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )

USE_MOCK_DATA = is_bool(os.getenv('API_USE_MOCK_DATA', 'True'))
