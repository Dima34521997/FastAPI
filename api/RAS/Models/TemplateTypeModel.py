from sqlmodel import SQLModel, Field


class TemplateType(SQLModel, table=True):
    Id: int = Field(primary_key=True)
    DeviceTypeId: int
    TemplatePath: str