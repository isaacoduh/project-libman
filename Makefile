test:
	python -m pytest tests/

build:
	docker compose -f docker-compose.yml up --build -d --remove-orphans

up:
	docker compose -f docker-compose.yml up -d

down:
	docker compose -f docker-compose.yml down

down-v:
	docker compose -f docker-compose.yml down -v

libman-config:
	docker compose -f docker-compose.yml config

makemigrations:
	docker compose -f docker-compose.yml run --rm api python manage.py makemigrations

migrate:
	docker compose -f docker-compose.yml run --rm api python manage.py migrate

collectstatic:
	docker compose -f docker-compose.yml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f docker-compose.yml run --rm api python manage.py createsuperuser

flush:
	docker compose -f docker-compose.yml run --rm api python manage.py flush