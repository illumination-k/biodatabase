.PHYNY: db
db: ## start db
	@docker compose -f docker-compose.db.yml up

.PHONY: backend
backend: ## run backend local
	@cd backend && pipenv run uvicorn main:app --reload --host=0.0.0.0 --port=8002
