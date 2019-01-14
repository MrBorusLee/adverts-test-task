down:
	docker-compose down --remove-orphans

clean:
	make down
	docker-compose build --pull

dev:
	docker-compose up --build

generate_fake_data:
	docker-compose exec web python manage.py generate_fake_data
