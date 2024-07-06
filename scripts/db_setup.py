from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BitcoinPrice(Base):
    __tablename__ = 'bitcoin_prices'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    price = Column(Float)

engine = create_engine('sqlite:///bitcoin.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def save_to_db(df):
    for index, row in df.iterrows():
        price = BitcoinPrice(timestamp=row['timestamp'], price=row['price'])
        session.add(price)
    session.commit()

save_to_db(df)
