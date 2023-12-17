.PHONY: up-services
up-services:
	docker-compose -f ./docker-compose.yml -p summarizer up

.PHONY: rebuild
rebuild:
	docker-compose -f ./docker-compose.yml -p summarizer up --build

.PHONY: up
up: rebuild

.PHONY: down
down:
	docker-compose -f ./docker-compose.yml -p summarizer down
