from typing import Literal, Optional
from sqlmodel import Field, SQLModel

class MediaAttachment(SQLModel, table=True):
    id: int = Field(primary_key=True)
    blurhash: str
    description: str
    meta: dict
    preview_url: str
    remote_url: str
    type: Literal['unknown', 'image', 'gifv', 'video', 'audio']
    url: str
