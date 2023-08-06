from typing import Optional, Literal, List, TYPE_CHECKING
from datetime import datetime
from sqlmodel import Field, SQLModel
from bs4 import BeautifulSoup

if TYPE_CHECKING:
    from diyalgo.models import Account, MediaAttachment, Tag, CustomEmoji, Poll


class Mention(SQLModel, table=True):
    acct: str
    id: int
    url: str
    username: str

class Status(SQLModel, table=True):
    """
    Model of a toot on mastodon

    See: https://mastodonpy.readthedocs.io/en/stable/#toot-dicts
    """
    id: int = Field(primary_key=True)
    application: Optional[dict] = None

    account: 'Account'
    bookmarked: Optional[bool] = None
    content: str
    created_at: datetime
    edited_at: Optional[datetime] = None
    emojis: List['CustomEmoji'] = Field(default_factory=list)
    favourited: Optional[bool] = None
    favourites_count: int
    filtered: Optional[List[str]] = Field(default_factory=list)
    in_reply_to_id: int
    in_reply_to_account_id: int
    language: Optional[str] = None
    media_attachments: List['MediaAttachment'] = Field(default_factory=list)
    mentions: List[Mention] = Field(default_factory=list)
    muted: Optional[bool] = None
    pinned: Optional[bool] = None
    poll: Optional['Poll'] = None
    reblog: bool
    reblogged: Optional[bool] = None
    reblogs_count: int
    replies_count: int
    sensitive: bool
    spoiler_text: str
    tags: List['Tag'] = Field(default_factory=list)
    text: Optional[str] = None
    uri: str
    url: str
    visibility: Literal['public', 'unlisted', 'private', 'direct']
    in_reply_to_id: Optional[int] = None
    in_reply_to_account_id: Optional[int] = None

    @property
    def soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.content)


    class Config:
        extra='ignore'

