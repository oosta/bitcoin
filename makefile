.PHONY: all setup fetch_data db_setup data_analysis

all: setup fetch_data db_setup data_analysis

setup:
	@echo "Setting up virtual environment and installing dependencies..."
	.\venv\Scripts\activate && pip install -r requirements.txt

fetch_data: setup
	@echo "Running fetch_data.py..."
	.\venv\Scripts\activate && python scripts/fetch_data.py

db_setup: fetch_data
	@echo "Creating data directory if it does not exist..."
	if not exist ..\data mkdir ..\data
	@echo "Running db_setup.py..."
	.\venv\Scripts\activate && python scripts/db_setup.py

data_analysis: db_setup
	@echo "Running data_analysis.py..."
	.\venv\Scripts\activate && python scripts/data_analysis.py