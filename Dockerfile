# Official Python image (Docker Hub). Avoids mcr.microsoft.com/devcontainers/* pull issues in Codespaces.
FROM python:3.12-bookworm

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
