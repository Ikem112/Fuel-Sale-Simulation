from pump_class import FuelPump
import random
import numpy as np
from faker import Faker
from tqdm import tqdm
from datetime import datetime

fake = Faker()
pump = FuelPump()


calendar = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

month = 1
while month <= 12:
    cal_month = calendar.get(month)
    for i in tqdm(range(1, cal_month + 1)):
        count = random.randint(150, 300)
        amount_ranges = [
            (1_000.0, 5_500.0, 500),
            (5_000.0, 15_500.0, 500),
            (15_000.0, 30_500.0, 500),
            (30_000.0, 50_500.0, 500),
        ]
        amount_weights = [0.3, 0.4, 0.2, 0.1]
        overflow_ranges = [
            (0.0, 10.1, 0.1),
            (10.1, 25.1, 0.1),
            (25.1, 40.1, 0.1),
            (40.1, 50.1, 0.1),
        ]
        overflow_weights = [55, 20, 18, 7]

        selected_a_range = random.choices(
            amount_ranges, weights=amount_weights, k=count
        )
        selected_o_range = random.choices(
            overflow_ranges, weights=overflow_weights, k=count
        )
        ss_date = datetime(year=2023, month=month, day=i, hour=5)
        se_date = datetime(year=2023, month=month, day=i, hour=22)
        rec_date = fake.date_time_between(start_date=ss_date, end_date=se_date)
        for chosen_a_range, chosen_o_range in zip(selected_a_range, selected_o_range):
            amount_float_range = np.arange(*chosen_a_range)
            random_a_float = random.choice(amount_float_range)
            overflow_float_range = np.arange(*chosen_o_range)
            random_o_float = random.choice(overflow_float_range)

            pump.fill_tank(random_a_float, random_o_float, rec_date)

    month += 1

    print(f"Data upload successfully completed...")
