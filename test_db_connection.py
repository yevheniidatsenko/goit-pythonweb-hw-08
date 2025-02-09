from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from src.conf.config import settings

def test_db_connection():
    # Get database_url from settings
    database_url = settings.database_url

    try:
        # Create a connection to the database
        engine = create_engine(database_url)
        with engine.connect() as connection:
            # Execute a simple query to test the connection
            result = connection.execute(text("SELECT 1"))
            print("Database connection successful! Test query result:", result.scalar())

    except SQLAlchemyError as e:
        print("Database connection error:", e)

if __name__ == "__main__":
    test_db_connection()