.PHONY: setup test lint run build docker-build clean

setup:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ --cov=src --cov-report=html

lint:
	flake8 src tests
	mypy src

run:
	python src/main.py

docker-build:
	docker build -t aura-engine:latest -f docker/Dockerfile .

docker-run:
	docker-compose -f docker/docker-compose.yml up

clean:
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	rm -rf .mypy_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +
