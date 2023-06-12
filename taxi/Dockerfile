# syntax=docker/dockerfile:1
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a group and user
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN groupadd -g ${GROUP_ID} appgroup && \
    useradd -m -l -u ${USER_ID} -g appgroup appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"

# Change to the new user
USER appuser

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . .
COPY --chown=appuser:appgroup . .
