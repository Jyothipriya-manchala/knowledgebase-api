from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class NoteDB(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)