import os.path
from docxtpl import DocxTemplate
from Models.InputDataModel import *



class DataRas:
    def __init__(self, json: InputData):

        self.results, self.header, self.name = \
            json.Results, json.Header, json.DeviceName.__dict__['Name']

        self.templates_path = '/home/dima/rasmaker_docker/api/RAS/Templates/'

        self.templates = os.listdir(self.templates_path)

        for device in self.templates:
            if self.name.lower() in device.lower():
                self.template = self.templates_path + device

        self.MSL = DocxTemplate(self.template)
        self.save_dir: str = os.path.join(os.getcwd(), "Templates", "МСЛ", "")


"""
{
   "Results":[
      {
         "OrderOperation":1,
         "ResponsibleFullName":"Терентиев Владимир Александрович",
         "EndTime":"2024-10-11",
         "Received":20,
         "Returned":20,
         "Notes":""
      },
      {
         "OrderOperation":2,
         "ResponsibleFullName":"Терентиев Владимир Александрович",
         "EndTime":"2024-10-11",
         "Received":20,
         "Returned":20,
         "Notes":""
      },
      {
         "OrderOperation":5,
         "ResponsibleFullName":"Терентиев Владимир Александрович",
         "EndTime":"2024-10-11",
         "Received":20,
         "Returned":17,
         "Notes":""
      }
   ],
   "Header":{
      "RasNumber":12,
      "Amount":20,
      "DeviceManNumbers":"1101 - 1200"
   },
   "DeviceName":{
      "Name":"пи_026-04"
   }
}
"""