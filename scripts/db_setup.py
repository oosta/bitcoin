import os
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from fetch_data import fetch_bitcoin_data  # Import the function from fetch_data

# Ensure the data directory exists
if not os.path.exists('../data'):
    os.makedirs('../data')

Base = declarative_base()

class BitcoinPrice(Base):
    __tablename__ = 'bitcoin_prices'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    price = Column(Float)

def save_to_db(df):
    engine = create_engine('sqlite:///../data/bitcoin.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for index, row in df.iterrows():
        price = BitcoinPrice(timestamp=row['timestamp'], price=row['price'])
        session.add(price)
    session.commit()
    session.close()

if __name__ == "__main__":
    df = fetch_bitcoin_data()
    save_to_db(df)
    print("Data saved to database successfully.")