from pydantic import BaseModel

class DeviceName(BaseModel):
    Name: str


class Header(BaseModel):
    RasNumber: int
    Amount: int
    DeviceManNumbers: str


class Result(BaseModel):
    OrderOperation: int
    ResponsibleFullName: str
    EndTime: str
    Received: int
    Returned: int
    Notes: str


class InputData(BaseModel):
    Results: list[Result]
    Header: Header
    DeviceName: DeviceName

"""
{
  "Results": [
    {
      "OrderOperation": 1,
      "ResponsibleFullName": "Терентиев Владимир Александрович",
      "EndTime": "2024-10-11",
      "Received": 20,
      "Returned": 20,
      "Notes": ""
    },
    {
      "OrderOperation": 2,
      "ResponsibleFullName": "Терентиев Владимир Александрович",
      "EndTime": "2024-10-11",
      "Received": 20,
      "Returned": 20,
      "Notes": ""
    },
    {
      "OrderOperation": 5,
      "ResponsibleFullName": "Терентиев Владимир Александрович",
      "EndTime": "2024-10-11",
      "Received": 20,
      "Returned": 17,
      "Notes": ""
    }
  ],
  
  "Header": 
  {
    "RasNumber": 12,
    "Amount": 20,
    "DeviceManNumbers": "1101 - 1200"
  },
  
  "DeviceName": 
  {
    "Name": "пи_026-04"
  }
}
"""
