# Adverts project
Abstract adverts application with views count which implemented using redis set.  
Project contains:
- Django backend
- PostgreSQL
- Redis
- Celery

## Basic idea of counter
- views counter for advert is stored in its model
- when user comes to advert page, system sets his id (if authenticated) or IP address to redis set, created for that advert
- once per X seconds celery task puts set size for every advert if it was changed

## Installation
Before you start, make sure that you have [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/) installed on your machine  
`make dev`  
It will run two development server at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Testing
To fill database with fake data use (while container is running)  
`make generate_fake_data` 