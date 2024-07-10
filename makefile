.PHONY: all setup_env fetch_fear_greed fetch_price fetch_volume fetch_google_trends fetch_data db_setup verify_db analyze

all: setup_env fetch_fear_greed fetch_price fetch_volume fetch_google_trends fetch_data analyze

setup_env:
	@echo "Setting up virtual environment and installing dependencies..."
	.\venv\Scripts\activate && pip install -r requirements.txt

fetch_price:
	@echo "Running fetch_price.py..."
	.\venv\Scripts\activate && python scripts/fetch_price.py

fetch_fear_greed:
	@echo "Running fetch_fear_greed.py..."
	.\venv\Scripts\activate && python scripts/fetch_fear_greed.py

fetch_volume:
	@echo "Running fetch_volume.py..."
	.\venv\Scripts\activate && python scripts/fetch_volume.py

fetch_google_trends:
	@echo "Running fetch_google_trends.py..."
	.\venv\Scripts\activate && python scripts/fetch_google_trends.py

fetch_data:
	@echo "Running fetch_data.py..."
	.\venv\Scripts\activate && python scripts/fetch_data.py

analyze:
	@echo "Running data_analysis.py..."
	.\venv\Scripts\activate && python scripts/data_analysis.py
