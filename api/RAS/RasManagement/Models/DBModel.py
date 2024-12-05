from sqlmodel import (Field,
                      Session,
                      SQLModel,
                      create_engine,
                      select)



class Table(SQLModel, table=True):
    FileName: str = Field(primary_key=True)
    FilePath: str
    FileDatetime: str
    FileType: str