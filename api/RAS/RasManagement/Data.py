import os.path
from docxtpl import DocxTemplate
from Models.InputDataModel import *


class DataRas:
    def __init__(self, json_data: InputData):

        self.results, self.header = \
            json_data.Results, json_data.Header

        self.template =\
            ('/home/dima/rasmaker_docker/api/RAS/RasManagement/Templates/'
             'Маршрутно-сопроводительный лист для ПИ 026-04.docx')
        self.MSL = DocxTemplate(self.template)
        self.save_dir: str = os.path.join(os.getcwd(), "Templates", "МСЛ", "")

