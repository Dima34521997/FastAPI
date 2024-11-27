#!/bin/bash
source /run/secrets/api-db-connection

set -e

psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
	CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
	CREATE DATABASE $DB_NAME OWNER $DB_USER;
EOSQL

psql -v ON_ERROR_STOP=1 --username "$DB_USER" --dbname "$DB_NAME" <<-EOSQL
	CREATE TABLE file (
          id int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
          path            text NOT NULL,
          time_created    int NOT NULL,
          content_hash    text NOT NULL
        );
EOSQL