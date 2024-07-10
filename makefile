.PHONY: all fetch_data fetch_fear_greed db_setup verify_db analyze

all: fetch_fear_greed fetch_data db_setup verify_db analyze

fetch_data:
	@echo "Running fetch_data.py..."
	.\venv\Scripts\activate && python scripts/fetch_data.py

fetch_fear_greed:
	@echo "Running fetch_fear_greed.py..."
	.\venv\Scripts\activate && python scripts/fetch_fear_greed.py

db_setup:
	@echo "Running db_setup.py..."
	.\venv\Scripts\activate && python scripts/db_setup.py

verify_db:
	@echo "Running verify_db.py..."
	.\venv\Scripts\activate && python scripts/verify_db.py

analyze:
	@echo "Running data_analysis.py..."
	.\venv\Scripts\activate && python scripts/data_analysis.py