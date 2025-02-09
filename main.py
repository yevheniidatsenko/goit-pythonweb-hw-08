from fastapi import FastAPI
import os
from alembic import command
from alembic.config import Config
import asyncio

# Import routes
from src.api import contacts, utils

app = FastAPI()

# Connect routes
app.include_router(contacts.router, prefix="/api")
app.include_router(utils.router, prefix="/api")

# Function to apply migrations
async def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

# Run migrations at application startup
@app.on_event("startup")
async def startup_event():
    await run_migrations()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)