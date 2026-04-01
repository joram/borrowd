# Stage 1: Build frontend assets
FROM node:22-slim AS frontend
WORKDIR /app
COPY package*.json vite.config.mjs ./
RUN npm ci
COPY static/ ./static/
COPY templates/ ./templates/
RUN npm run build

# Stage 2: Python application
FROM python:3.13-slim
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .
COPY --from=frontend /app/build ./build

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "borrowd.wsgi:application"]
