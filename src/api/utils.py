from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.database.database import get_db

router = APIRouter(tags=["utils"])

@router.get("/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        # Execute a simple SQL query to check the database connection
        result = await db.execute(text("SELECT 1"))
        result = result.scalar_one_or_none()

        # If the query result is not as expected, raise an error
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database is not configured correctly",
            )

        # If everything is fine, return a success message
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        # Log the error (for debugging convenience)
        print(e)
        # Raise an error if something went wrong
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error connecting to the database",
        )