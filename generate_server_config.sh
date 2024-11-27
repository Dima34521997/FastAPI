#!/bin/bash
eval "$(cat secrets/db-connection | tr "\n" " ") envsubst '\$DB_NAME \$DB_USER' < configs/servers_template.json > configs/servers.json"