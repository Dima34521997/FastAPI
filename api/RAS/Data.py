import os.path
from docxtpl import DocxTemplate
from Models.InputDataModel import *


class DataRas:
    def __init__(self, json: InputData):

        self.results, self.header, self.ID = \
            json.Results, json.Header, json.DeviceType.__dict__['ID']


        self.template_names = {1: 'ПИ_026-04.docx',
                               2: 'ПИ_026-02.docx',
                               3: 'ПИ_004.docx',
                               4: 'Датчик_глаза.docx',
                               5: 'МТП.docx',
                               }


        self.template =\
            (f'/home/dima/rasmaker_docker/api/RAS/RasManagement/Templates/'
             f'{self.template_names[self.ID]}')


        self.MSL = DocxTemplate(self.template)
        self.save_dir: str = os.path.join(os.getcwd(), "Templates", "МСЛ", "")

