from argparse import FileType

from fastapi import FastAPI
from pydantic import FilePath

from Executor import *
from fastapi.responses import FileResponse
from sqlmodel import create_engine, Session
from Models.FileModel import Table

app = FastAPI()
db_url = "postgresql://api:12345@db/rasmaker"
engine = create_engine(db_url, echo=True)


@app.get("/home")
async def home_page():
    return {"key": "value"}


@app.post("/makeras")
async def make_ras(json_data: InputData) -> FileResponse:
    return FileResponse(execute(json_data))


@app.post("/addelement")
async def add_element(file_name: str,
                      file_path: str,
                      file_datetime: str,
                      file_type: str):
    with Session(engine) as session:
        field = Table(FileName=file_name, FilePath=file_path,
                      FileDatetime=file_datetime, FileType=file_type)

        session.add(field)
        session.commit()
