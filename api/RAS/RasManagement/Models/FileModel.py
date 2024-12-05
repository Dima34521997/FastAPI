from sqlmodel import (Field,
                      Session,
                      SQLModel,
                      create_engine,
                      select)



class File(SQLModel, table=True):
    """ Планируется 3 таблицы: с файлами-результатами,
    с шаблонами и с типами
    """

    Id: int = Field(primary_key=True)
    Name: str
    Path: str # путь на папку где хранится итоговый документ
    TypeId: int = Field(foreign_key='FileType.Id')
    # TypeId просто ссылает на связанную таблицу FileType
