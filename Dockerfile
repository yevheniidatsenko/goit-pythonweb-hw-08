# Choose the base image with Python 3.12
FROM python:3.12-slim

# Install necessary system packages for Poetry, dependency compilation, and psycopg2
RUN apt-get update && apt-get install -y gcc curl libpq-dev python3-dev

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Create and move to the working directory
WORKDIR /src

# Copy project files to the container
COPY pyproject.toml poetry.lock ./
COPY . .

# Copy .env file (if it exists)
COPY .env .env

# Install dependencies via Poetry (without dev-dependencies)
RUN poetry install --no-interaction --only main --no-root

# Expose the port that the application will use
EXPOSE 8000

# Start the server
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]