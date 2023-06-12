# This Makefile provides several commands for managing your Docker containers:

UID=$(shell id -u)
GID=$(shell id -g)

# Builds your Docker images.
build:
	HOST_UID=${UID} HOST_GID=${GID} docker-compose -f docker-compose.dev.yml build

# Stop your Docker images.
stop:
	HOST_UID=${UID} HOST_GID=${GID} docker-compose -f docker-compose.dev.yml stop

# Runs your test Docker container in attached mode.
test:
	HOST_UID=${UID} HOST_GID=${GID} docker-compose -f docker-compose.dev.yml up --abort-on-container-exit test

# Runs your web Docker container in attached mode.
web-attached:
	HOST_UID=${UID} HOST_GID=${GID} docker-compose -f docker-compose.dev.yml up web

# Runs your web Docker container in detached mode.
web-detached:
	HOST_UID=${UID} HOST_GID=${GID} docker-compose -f docker-compose.dev.yml up -d web

# Runs your web Docker container in detached mode and enters its bash shell.
web-bash:
	HOST_UID=${UID} HOST_GID=${GID} docker-compose -f docker-compose.dev.yml up -d web && \
	docker-compose -f docker-compose.dev.yml exec web bash

# DELETES AND BUILD
clean-build:
	HOST_UID=${UID} HOST_GID=${GID} docker-compose -f docker-compose.dev.yml  down --volumes && docker-compose -f docker-compose.dev.yml build
