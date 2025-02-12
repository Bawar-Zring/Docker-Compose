# Docker-Compose
containerize Flask app, PostgreSQL and Redis.

  ---------------------------

remember to create you own environment variable folder /env/app.env & /env/db.env

  ---------------------------

1. Creating a `Dockerfile` to containerize the Flask app, use bind mound volume to in sure if change in app.py occurs don't need to rebuild image.
2. Writing a `docker-compose.yml` file to orchestrate the app, PostgreSQL(use named volume to store data persistently), and Redis.

  ---------------------------

how to run

run:
docker-compose up -d --build

test:
curl http://localhost/health

the result should be:
1. "connected to both redis and database"        Good
2. "connected to database"                       Error
3. "connected to redis"                          Error
