import os.path
from Models.InputDataModel import InputData
from Data import DataRas


def execute(json_data: InputData):
    data = DataRas(json_data)
    context = dict()

    for string in data.results:
        order = str(string.OrderOperation)

        context["ResponsibleFullName" + order] = string.ResponsibleFullName
        context["EndTime" + order] = string.EndTime
        context["Received" + order] = string.Received
        context["Returned" + order] = string.Returned
        context["Notes" + order] = string.Notes

    context = {**context, **data.header.__dict__}
    data.MSL.render(context)
    if not os.path.exists(data.save_dir):
        os.makedirs(data.save_dir)

    data.MSL.save(os.path.join(data.save_dir, os.path.split(data.template)[-1]))
    return os.path.join(data.save_dir, os.path.split(data.template)[-1])