from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a base class for models
Base = declarative_base()

# Define a model (table)
class Fuel_Sales_2023(Base):
    __tablename__ = "fuel_sales_2023"

    id = Column(Integer, primary_key=True)
    amount_paid = Column(Float, nullable=False)
    amount_recorded = Column(Float, nullable=False)
    amount_overflow = Column(Float, nullable=False)
    rate_per_litre = Column(Float, nullable=False)
    litres_paid = Column(Float, nullable=False)
    litres_recorded = Column(Float, nullable=False)
    litres_overflow = Column(Float, nullable=False)
    time_issued = Column(DateTime, nullable=False)
    station_region = Column(String, nullable=False)
