from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    days = relationship("Day", back_populates="owner", cascade="all, delete-orphan")


class Day(Base):
    __tablename__ = "days"
    __table_args__ = (UniqueConstraint("owner_id", "date", name="uq_owner_date"),)

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, index=True)  # YYYY-MM-DD, one row per user per day
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="days")
    entries = relationship(
        "EmotionEntry", back_populates="day", cascade="all, delete-orphan", order_by="EmotionEntry.id"
    )


class EmotionEntry(Base):
    __tablename__ = "emotion_entries"

    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("days.id"), nullable=False)

    primary_emotion = Column(String, nullable=False)
    secondary_emotion = Column(String, nullable=False)
    tertiary_emotion = Column(String, nullable=True)  # optional, per spec
    note = Column(String, nullable=True)  # thought/situation behind the feeling

    created_at = Column(DateTime, server_default=func.now())

    day = relationship("Day", back_populates="entries")
