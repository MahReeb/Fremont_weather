import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

latitude = 54.644514
longitude = 45.454155

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
print(response.status_code)

data = response.json()

print(data)

#-------------------------------------------------------------------

daily_data = data["daily"]

df = pd.DataFrame({
    "date" : daily_data["time"],
    "max_temp" : daily_data["temperature_2m_max"],
    "min_temp" : daily_data["temperature_2m_min"]
})

df["date"] = pd.to_datetime(df["date"])

print(df)

#------------------------------------------------------------------

plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max_temp"], marker = "x", label = "Max Temperature")
plt.plot(df["date"], df["min_temp"], marker = "o", label = "Min Temperature")

plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.title("Fremont Weather - Past 7 Days")
plt.legend()

plt.xticks(rotation = 30)
plt.tight_layout()

plt.savefig("Weather_Chart.png")
plt.show

