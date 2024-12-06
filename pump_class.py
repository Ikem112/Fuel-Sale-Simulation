import os
from db_models import Fuel_Sales_2023
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


class FuelPump:
    def __init__(self) -> None:
        self.fuel_station = "Enyo"
        self.rate_per_naira = 0.00187793
        self.rate_per_litre = 532.50
        self.engine = create_engine(os.getenv("DATABASE_URI"))
        self.Session = sessionmaker(bind=self.engine)

    def fill_tank(self, amount: float, overflow: float, rec_date):
        litres_paid = amount / self.rate_per_litre
        amount_gotten = amount + overflow
        litres_gotten = amount_gotten / self.rate_per_litre
        litre_overflow = litres_gotten - litres_paid

        testing = True

        if testing:
            print(
                f"{amount}\n{amount_gotten}\n{overflow}\n{self.rate_per_litre}\n{litres_paid}\n{litres_gotten}\n{litre_overflow}\n{rec_date}"
            )
        else:
            session = self.Session()
            try:
                new_record = Fuel_Sales_2023(
                    amount_paid=amount,
                    amount_recorded=amount_gotten,
                    amount_overflow=overflow,
                    rate_per_litre=self.rate_per_litre,
                    litres_paid=litres_paid,
                    litres_recorded=litres_gotten,
                    litres_overflow=litre_overflow,
                    time_issued=rec_date,
                    station_region="Lagos",
                )
                session.add(new_record)
                session.commit()

            except Exception as e:
                session.rollback()
                print("Error occurred:", e)

            finally:
                session.close()
