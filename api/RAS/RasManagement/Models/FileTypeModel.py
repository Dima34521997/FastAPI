from sqlalchemy.orm import foreign
from sqlmodel import SQLModel, Field


class FileType(SQLModel, table=True):
    Id: int = Field(primary_key=True)
    Name: str # Имя файла, которое получится после генерации
