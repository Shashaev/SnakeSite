import pydantic


class StatusOk(pydantic.BaseModel):
    status: str = 'ok'


class UserData(pydantic.BaseModel):
    username: str = pydantic.Field(min_length=1)
    password: str = pydantic.Field(min_length=30)


class Note(pydantic.BaseModel):
    id_model: int
    title: str = pydantic.Field(
        min_length=1,
        strict=True,
        examples=['Медянка', 'Обыкновенный уж', 'Гадюка обыкновенная'],
    )
    description: str = pydantic.Field(
        min_length=1,
        strict=True,
    )
    image: str = pydantic.Field(
        min_length=1,
        strict=True,
    )
    is_user: bool
