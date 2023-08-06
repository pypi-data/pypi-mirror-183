from sqlmodel import Field, SQLModel

class Tag(SQLModel, table=True):
    name: str
    url: str