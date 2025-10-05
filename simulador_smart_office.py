import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parâmetros
start_date = datetime(2025, 9, 1, 0, 0)
end_date = start_date + timedelta(days=7)
time_range = pd.date_range(start=start_date, end=end_date, freq="15min")

data = []

for ts in time_range:
    # Temperatura (°C)
    if 6 <= ts.hour <= 18:
        temp = np.random.normal(23, 1.5)  # mais quente de dia
    else:
        temp = np.random.normal(20, 1.0)  # mais frio à noite
    
    # Luminosidade (lux)
    if 6 <= ts.hour <= 18:
        lux = np.random.normal(300, 50)   # luz do dia
    else:
        lux = 0   # noite
    
    # Ocupação (1=ocupado, 0=livre)
    if ts.weekday() < 5 and 8 <= ts.hour <= 18:
        ocupacao = np.random.choice([0, 1], p=[0.3, 0.7])
    else:
        ocupacao = np.random.choice([0, 1], p=[0.9, 0.1])
    
    data.append([ts, "sensor_temp", round(temp,2)])
    data.append([ts, "sensor_lux", round(lux,2)])
    data.append([ts, "sensor_ocupacao", ocupacao])

# Criar DataFrame
df = pd.DataFrame(data, columns=["timestamp", "sensor_id", "valor"])
df.to_csv("smart_office_data.csv", index=False)

print("Arquivo smart_office_data.csv gerado com sucesso!")
