from app import db

from .base import TimestampedDatabaseModel
from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .task import Task


class BoardStatus(Enum):
    ARCHIVED = "archived"
    OPEN = "open"


class Board(TimestampedDatabaseModel):
    __tablename__ = 'board'

    status: Mapped[str] = mapped_column(db.String, default=BoardStatus.OPEN.value)

    tasks: Mapped[list['Task']] = db.relationship(
        back_populates="board",
        lazy="selectin",
        uselist=True,
        cascade="all, delete",
    )
