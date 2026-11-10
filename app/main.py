from fastapi import FastAPI
from sqlalchemy import text

from .db import Session

app = FastAPI(title="CourseTube")


@app.get("/health")
async def health(session: Session):
    await session.scalar(text("SELECT 1"))
    return {"status": "ok"}
