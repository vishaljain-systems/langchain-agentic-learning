.PHONY: help install test lint format type-check clean run-example

help:
	@echo "LangChain Agentic Learning Repository"
	@echo ""
	@echo "Commands:"
	@echo "  make install         Install dependencies"
	@echo "  make test            Run all tests"
	@echo "  make test-fast       Run fast subset of tests"
	@echo "  make coverage        Generate coverage report"
	@echo "  make lint            Check code style with ruff"
	@echo "  make format          Auto-format code with black"
	@echo "  make type-check      Type checking with mypy"
	@echo "  make clean           Remove build artifacts"
	@echo "  make example         Run a specific example"
	@echo ""

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v

test-fast:
	pytest tests/ -v -m "not slow"

coverage:
	pytest tests/ --cov=. --cov-report=html
	@echo "Coverage report: htmlcov/index.html"

lint:
	ruff check . --select=E,W,F

format:
	black . --line-length=100

type-check:
	mypy . --ignore-missing-imports

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info
	rm -rf .pytest_cache .coverage htmlcov

example:
	@echo "Usage: make example EXAMPLE=01_fundamentals/01_llm_basics.py"
	python3 $(EXAMPLE)

.DEFAULT_GOAL := help
