from pydantic import BaseModel, AnyHttpUrl
from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional, List
from bs4 import BeautifulSoup

from diyalgo.models import CustomEmoji

class AccountField(BaseModel):
    name: str
    value: str
    verified_at: Optional[datetime] = None
    url: Optional[AnyHttpUrl] = None

    def __init__(self, name:str, value:str, verified_at:Optional[datetime] = None):
        soup = BeautifulSoup(value, 'lxml')
        a = soup.find('a')
        if a is not None:
            url = a.get('href')
        else:
            url = None
        super().__init__(name=name, value=value, url=url, verified_at=verified_at)

    class Config:
        extra = "ignore"


class Account(SQLModel, table=True):
    """https://docs.joinmastodon.org/entities/Account/"""
    id: int = Field(primary_key=True)
    acct: str
    avatar: str
    avatar_static: str
    bot: bool
    created_at:datetime
    discoverable:bool
    display_name:str
    emojis: List[CustomEmoji] = Field(default_factory=list)
    fields: List[AccountField] = Field(default_factory=list)
    followers_count:int
    following_count:int
    group: bool
    header: str
    last_status_at: Optional[datetime] = None
    limited: Optional[bool] = None
    locked: bool
    moved: Optional['Account'] = None
    noindex: Optional[bool] = None
    header_static: str
    note: str
    statuses_count: int
    suspended: Optional[bool] = None
    url: AnyHttpUrl
    username: str

    class Config:
        extra = 'ignore'