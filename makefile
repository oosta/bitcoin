# Makefile

.PHONY: all setup fetch_data db_setup verify_db analyze

all: setup fetch_data db_setup verify_db analyze

setup:
	@echo "Setting up virtual environment and installing dependencies..."
	.\venv\Scripts\activate && pip install -r requirements.txt

fetch_data:
	@echo "Running fetch_data.py..."
	.\venv\Scripts\activate && python scripts/fetch_data.py

db_setup:
	@echo "Running db_setup.py..."
	.\venv\Scripts\activate && python scripts/db_setup.py

verify_db:
	@echo "Running verify_db.py..."
	.\venv\Scripts\activate && python scripts/verify_db.py

analyze:
	@echo "Running data_analysis.py..."
	.\venv\Scripts\activate && python scripts/data_analysis.py