from pydantic import BaseModel, Field
from datetime import date as date_type, datetime
from typing import Optional


# ---------- Auth ----------

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=128)


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str


# ---------- Emotion entries ----------

class EmotionEntryCreate(BaseModel):
    primary_emotion: str
    secondary_emotion: str
    tertiary_emotion: Optional[str] = None
    note: Optional[str] = Field(default=None, max_length=2000)


class EmotionEntryOut(BaseModel):
    id: int
    primary_emotion: str
    secondary_emotion: str
    tertiary_emotion: Optional[str]
    note: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


# ---------- Days ----------

class DayOut(BaseModel):
    id: int
    date: date_type
    entries: list[EmotionEntryOut]

    class Config:
        from_attributes = True


class DaySummary(BaseModel):
    """Lightweight version for calendar/heatmap views."""
    date: date_type
    entry_count: int
    primary_emotions: list[str]  # for color-coding a calendar cell
