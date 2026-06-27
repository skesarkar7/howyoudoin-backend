import os
from datetime import date as date_type

from dotenv import load_dotenv
load_dotenv()  # no-op in production if no .env file exists; Railway injects env vars directly

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import engine, get_db, Base
import models
import schemas
import auth
from emotions_data import EMOTIONS

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Emotion Journal API")

# CORS: set FRONTEND_URL env var on Railway to your deployed Vercel URL.
# Local dev origins are included for convenience.
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]
frontend_url = os.getenv("FRONTEND_URL")
if frontend_url:
    origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok"}


# ---------------- Auth ----------------

@app.post("/auth/register", response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user_in.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")

    user = models.User(
        username=user_in.username,
        hashed_password=auth.hash_password(user_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return schemas.Token(
        access_token=auth.create_access_token(user.username),
        refresh_token=auth.create_refresh_token(user.username),
    )


@app.post("/auth/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    return schemas.Token(
        access_token=auth.create_access_token(user.username),
        refresh_token=auth.create_refresh_token(user.username),
    )


@app.post("/auth/refresh", response_model=schemas.Token)
def refresh(payload: schemas.RefreshRequest, db: Session = Depends(get_db)):
    username = auth.decode_token(payload.refresh_token, expected_type="refresh")
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    # Issue a new access token, and rotate the refresh token too.
    return schemas.Token(
        access_token=auth.create_access_token(user.username),
        refresh_token=auth.create_refresh_token(user.username),
    )


# ---------------- Emotion taxonomy (static reference data) ----------------

@app.get("/emotions")
def get_emotions():
    """Returns the full primary -> secondary -> tertiary taxonomy used to build the picker UI."""
    return EMOTIONS


# ---------------- Days & entries ----------------

def _get_or_create_day(db: Session, user: models.User, day: date_type) -> models.Day:
    day_row = (
        db.query(models.Day)
        .filter(models.Day.owner_id == user.id, models.Day.date == day)
        .first()
    )
    if not day_row:
        day_row = models.Day(date=day, owner_id=user.id)
        db.add(day_row)
        db.commit()
        db.refresh(day_row)
    return day_row


@app.get("/days/{day}", response_model=schemas.DayOut)
def get_day(day: date_type, db: Session = Depends(get_db), user: models.User = Depends(auth.get_current_user)):
    day_row = (
        db.query(models.Day)
        .filter(models.Day.owner_id == user.id, models.Day.date == day)
        .first()
    )
    if not day_row:
        # No entries yet for this date -- return an empty shell rather than 404,
        # since "no entries today" is a normal, expected state in a journal.
        return schemas.DayOut(id=0, date=day, entries=[])
    return day_row


@app.post("/days/{day}/entries", response_model=schemas.EmotionEntryOut, status_code=status.HTTP_201_CREATED)
def add_entry(
    day: date_type,
    entry_in: schemas.EmotionEntryCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(auth.get_current_user),
):
    if entry_in.primary_emotion not in EMOTIONS:
        raise HTTPException(status_code=400, detail="Unknown primary emotion")
    secondary_options = EMOTIONS[entry_in.primary_emotion]
    if entry_in.secondary_emotion not in secondary_options:
        raise HTTPException(status_code=400, detail="Unknown secondary emotion for this primary")
    if entry_in.tertiary_emotion is not None:
        if entry_in.tertiary_emotion not in secondary_options[entry_in.secondary_emotion]:
            raise HTTPException(status_code=400, detail="Unknown tertiary emotion for this secondary")

    day_row = _get_or_create_day(db, user, day)
    entry = models.EmotionEntry(day_id=day_row.id, **entry_in.model_dump())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


@app.patch("/entries/{entry_id}", response_model=schemas.EmotionEntryOut)
def update_entry_note(
    entry_id: int,
    update: schemas.EntryNoteUpdate,
    db: Session = Depends(get_db),
    user: models.User = Depends(auth.get_current_user),
):
    """Edits only the note on an existing entry -- the emotion selection itself is immutable by design."""
    entry = (
        db.query(models.EmotionEntry)
        .join(models.Day)
        .filter(models.EmotionEntry.id == entry_id, models.Day.owner_id == user.id)
        .first()
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    entry.note = update.note
    db.commit()
    db.refresh(entry)
    return entry


@app.delete("/entries/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_entry(
    entry_id: int, db: Session = Depends(get_db), user: models.User = Depends(auth.get_current_user)
):
    entry = (
        db.query(models.EmotionEntry)
        .join(models.Day)
        .filter(models.EmotionEntry.id == entry_id, models.Day.owner_id == user.id)
        .first()
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(entry)
    db.commit()
    return None


@app.get("/days", response_model=list[schemas.DaySummary])
def list_days(
    start: date_type,
    end: date_type,
    db: Session = Depends(get_db),
    user: models.User = Depends(auth.get_current_user),
):
    """Used by the calendar/heatmap view (phase 2 groundwork, but useful now too)."""
    day_rows = (
        db.query(models.Day)
        .filter(models.Day.owner_id == user.id, models.Day.date >= start, models.Day.date <= end)
        .all()
    )
    summaries = []
    for d in day_rows:
        if not d.entries:
            continue
        summaries.append(
            schemas.DaySummary(
                date=d.date,
                entry_count=len(d.entries),
                primary_emotions=[e.primary_emotion for e in d.entries],
            )
        )
    return summaries
