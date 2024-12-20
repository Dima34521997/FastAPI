from tempfile import template

from fastapi import FastAPI
from jinja2 import Template
from pydantic import FilePath

from Executor import *
from fastapi.responses import FileResponse
from sqlmodel import create_engine, Session

from Models.FileModel import File
from Models.FileTypeModel import FileType
from Models.TemplateTypeModel import TemplateType

from Data import DataRas

app = FastAPI()
db_url = "postgresql://api:12345@db/rasmaker"
engine = create_engine(db_url, echo=True)


@app.get("/home")
async def home_page():
    return {"key": "value"}


@app.post("/makeras")
async def make_ras(json_data: InputData) -> FileResponse:
    return FileResponse(execute(json_data))


@app.post("/add_element_file")
async def add_element_to_file(id: int,
                              name: str,
                              path: str,
                              datetime: str,
                              type_id: int):

    with Session(engine) as session:
        field = File(Id=id,
                     Name=name,
                     Path=path,
                     Datetime=datetime,
                     TypeId=type_id)

        session.add(field)
        session.commit()


@app.post("/add_element_file_type")
async def add_element_to_file_type(id: int, name: str):

    with Session(engine) as session:
        field = FileType(Id=id, Name=name)
        session.add(field)
        session.commit()


@app.post("/add_element_template_type")
async def add_element_to_template_type(id: int,
                                       device_type_id: str,
                                       template_path: str):

    with Session(engine) as session:
        field = TemplateType(Id=id,
                             DeviceTypeId=device_type_id,
                             emplatePath=template_path)

        session.add(field)
        session.commit()


# region Тест всякого
# templates_path = '/home/dima/rasmaker_docker/api/RAS/Templates/'
#
# templates = os.listdir(templates_path)
#
# name = 'пи_026-04'
#
# for device in templates:
#     if name.lower() in device.lower():
#         template = f'{templates_path}{device}'
#         print(template)
#
# print(templates)


# endregion
