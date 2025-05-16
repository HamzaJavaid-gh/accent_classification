# Makefile for Accent Classification Project

PYTHON=python
PIP=pip

# Default virtual environment folder
VENV=.venv

# Install dependencies
build:
	@echo "🔧 Installing dependencies..."
	$(PIP) install -r requirements.txt

# Run tests
test:
	@echo "✅ Running tests..."
	pytest -v tests/

# Clean Python bytecode and temporary files
clean:
	@echo "🧹 Cleaning up..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .pytest_cache
	rm -rf *.egg-info
