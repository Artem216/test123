debug:
	sudo docker compose -f deployment/docker-compose.yml up --build

deploy:
	docker compose -f deployment/docker-compose.yml up db --build -d