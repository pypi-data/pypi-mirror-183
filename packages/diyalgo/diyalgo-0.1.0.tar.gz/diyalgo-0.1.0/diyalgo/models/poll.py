from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel

if TYPE_CHECKING:
    from diyalgo.models import CustomEmoji

class PollOption(SQLModel):
    title: str
    votes_count: Optional[int] = None

class Poll(SQLModel, table=True):
    id: int = Field(primary_key=True)
    emojis: List['CustomEmoji'] = Field(default_factory=list)
    expires_at: Optional[datetime] = None
    expired: bool
    multiple: bool
    options: List[PollOption] = Field(default_factory=list)
    own_votes: List[int] = Field(default_factory=list)
    voted: Optional[bool] = None
    votes_count: int
    voters_count: Optional[int] = None
