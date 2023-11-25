from app import db

from .base import TimestampedDatabaseModel
from sqlalchemy.orm import Mapped, mapped_column

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .board import Board


class Task(TimestampedDatabaseModel):
    __tablename__ = 'task'

    is_completed: Mapped[bool] = mapped_column(db.Boolean, default=False)
    text: Mapped[str] = mapped_column(db.String)
    board_id: Mapped[str] = mapped_column(db.String(36), db.ForeignKey('board.id'))

    board: Mapped['Board'] = db.relationship(
        back_populates="tasks",
        lazy="selectin",
        uselist=False,
    )
