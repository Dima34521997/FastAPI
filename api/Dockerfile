FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Этот пакет нужен для корректного автоопределения content-type в FileResponse
RUN apt -y update && \
apt -y upgrade && \
apt -y install media-types

WORKDIR /usr/src/app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

COPY . .

CMD ["fastapi", "run", "RAS/RasManagement/main.py", "--port", "80"]
