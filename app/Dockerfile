FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml .
COPY app/ ./app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn grpcio grpcio-tools tenacity

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
