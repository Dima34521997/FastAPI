from fastapi import FastAPI
from Executor import *
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/home")
async def home_page():
    return {"key": "value"}


@app.post("/makeras")
async def make_ras(json_data: InputData) -> FileResponse:
    return FileResponse(execute(json_data))


