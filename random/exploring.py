# Neccessary imports
import fastf1
import pandas as pd
import matplotlib.pyplot as plt

# Enable the cache (so data is stored locally)
fastf1.Cache.enable_cache(r"C:\UNI\Code\F1_Race_Predictor")  # replace 'cache' with your desired cache directory

# Load Bahrain GP 2023 session data
session = fastf1.get_session(2023, 'Bahrain', 'Q')
session.load() # 'R' = Race ('Q' = Qualifying, 'FP1' = Free Practice 1, etc.)

# Filter Williams drivers (Albon, Sargeant)
williams_drivers = ['ALB', 'SAR']
results = session.results
williams_results = results[results['Abbreviation'].isin(williams_drivers)]

print(williams_results[['Abbreviation', 'GridPosition', 'Position', 'Status']])