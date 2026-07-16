# =========================
# Build Stage
# =========================
FROM python:3.9-slim as builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# =========================
# Production Stage
# =========================
FROM python:3.9-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean


# Create non-root user
RUN groupadd -r django && \
    useradd -r -g django django


# Copy virtual environment
COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"


WORKDIR /app


# Copy project files
COPY --chown=django:django . .


# SQLite database permission
RUN touch /app/db.sqlite3 && \
    chown -R django:django /app && \
    chmod -R 775 /app


# Run as django user
USER django


# Database migration
RUN python manage.py migrate


# Collect static files
RUN python manage.py collectstatic --noinput


EXPOSE 8000


HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python manage.py check --deploy


CMD ["gunicorn", "clinic.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--threads", "2"]