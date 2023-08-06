from sqlmodel import Field, SQLModel

class CustomEmoji(SQLModel, table=True):
    shortcode: str = Field(primary_key=True)
    url: str
    static_url: str
    visible_in_picker: bool
    category: str