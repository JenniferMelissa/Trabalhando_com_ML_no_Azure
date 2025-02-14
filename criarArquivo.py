import pandas as pd
import numpy as np

num_days = 365

data = {
    "day": np.tile(np.arange(1, 32), int(np.ceil(num_days / 31)))[:num_days],
    "mnth": np.tile(np.arange(1, 13), int(np.ceil(num_days / 12)))[:num_days],
    "year": np.full(num_days, 2024),
    "season": np.tile([1, 2, 3, 4], int(np.ceil(num_days / 4)))[:num_days],  # 1: inverno, 2: primavera, etc.
    "holiday": np.random.choice([0, 1], num_days, p=[0.95, 0.05]),  # 5% de feriados
    "weekday": np.tile(np.arange(7), int(np.ceil(num_days / 7)))[:num_days],
    "workingday": np.random.choice([0, 1], num_days, p=[0.3, 0.7]),  # 70% dias úteis
    "weathersit": np.random.choice([1, 2, 3], num_days, p=[0.6, 0.3, 0.1]),  # Clima bom na maioria dos dias
    "temp": np.round(np.random.uniform(0.1, 1.0, num_days), 2),  # Temperatura normalizada
    "hum": np.round(np.random.uniform(0.2, 0.9, num_days), 2),  # Umidade normalizada
    "windspeed": np.round(np.random.uniform(0.05, 0.5, num_days), 2),  # Velocidade do vento normalizada
    "energy_consumption": np.round(np.random.uniform(200, 2000, num_days), 2)  # Consumo diário de energia em kWh
}


df_energy = pd.DataFrame(data)

df_energy.to_csv("daily-energy-consumption.csv", index=False)



