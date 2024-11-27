#!/bin/bash

set -ve

source ./generate_server_config.sh

docker compose down -v
docker compose build --pull
docker compose up --remove-orphans --wait