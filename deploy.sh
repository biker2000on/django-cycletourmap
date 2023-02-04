#/bin/bash

docker compose -f docker-compose.prod.yml down
git checkout main
git pull
docker compose -f docker-compose.prod.yml up -d --build