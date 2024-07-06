from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import BitcoinPrice  # Import the BitcoinPrice model

def verify_data():
    engine = create_engine('sqlite:///../data/bitcoin.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(BitcoinPrice).all()
    for row in results:
        print(row.timestamp, row.price)
    
    session.close()

if __name__ == "__main__":
    verify_data()
