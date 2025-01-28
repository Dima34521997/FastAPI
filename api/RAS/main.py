import os.path
from pathlib import Path
from docxtpl import DocxTemplate
from fastapi import FastAPI, HTTPException
from sqlmodel import create_engine, Session

from Models.FileModel import File
from Models.FileTypeModel import FileType
from Models.InputDataModel import *
from Models.TemplateTypeModel import TemplateType

app = FastAPI()
db_url = "postgresql://api:12345@db/rasmaker"
engine = create_engine(db_url, echo=True)


@app.get("/home")
async def home_page():
    return {"key": "value"}


@app.post("/makeras", status_code=201)
async def make_ras(json_data: InputData) -> str:

    results, header, name = \
        json_data.Results, json_data.Header, json_data.DeviceName.__dict__['Name']
    '''Распарсили поступивший JSON'''

    # templates_path = '/home/dima/rasmaker_docker/api/RAS/Templates/'
    base_path = Path(__file__).resolve().parent
    print(base_path)
    templates_path = base_path.joinpath('Templates')
    '''Путь к папке с шаблонами'''

    templates = os.listdir(templates_path)
    '''Возвращает список, содержащий имена шаблонов в каталоге'''

    template_path = ''
    device_name: str = ''

    msl_num: str = json_data.Header.__dict__["RasNumber"]

    for device in templates:
        '''Ищем подходящий шаблон из списка'''
        if name:
            if name.lower() in device.lower():
                template_path = templates_path.joinpath(device)
                device_name = device.split('.')[0]
        else:
            raise HTTPException(status_code=601, detail="Ошибка JSON - пустой Name")

    if not template_path:
        raise HTTPException(status_code=602, detail="Не удалось найти подходящий шаблон")


    msl = DocxTemplate(template_path)
    save_dir: str = os.path.join(os.getcwd(), "Готовые МСЛ", "")

    context = dict()

    for string in results:
        order = str(string.OrderOperation)

        context["ResponsibleFullName" + order] = string.ResponsibleFullName
        context["EndTime" + order] = string.EndTime
        context["Received" + order] = string.Received
        context["Returned" + order] = string.Returned
        context["Notes" + order] = string.Notes

    context = {**context, **header.__dict__}

    msl.render(context)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # msl.save(os.path.join(save_dir, os.path.split(template)[-1]))
    msl.save(os.path.join(save_dir, f'МСЛ {device_name} № {msl_num}.docx'))
    #return FileResponse(os.path.join(save_dir, os.path.split(template)[-1]))
    return os.path.join(save_dir, os.path.split(template_path)[-1])


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
