from app import db

from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone
import uuid


class DatabaseModel(db.Model):
    __abstract__ = True

    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class UUIDModel(DatabaseModel):
    __abstract__ = True

    id: Mapped[str] = mapped_column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))


class TimestampedDatabaseModel(UUIDModel):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
