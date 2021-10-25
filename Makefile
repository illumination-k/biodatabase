.PHONY: backend.local
backend.local: # run backend local
	@cd backend && pipenv run uvicorn main:app --reload --host=0.0.0.0 --port=8002
