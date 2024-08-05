"""
Handles weather info
"""
# Imports
import requests
from datetime import datetime

# Config
API_KEY = "dc927b3a3f59d84bc844ae1a74ef648f"
CITY_NAME = "Glasgow"
COUNTRY_CODE = "uk"
ERROR_MSG = "Failed to get weather data"
KELVIN = 273.15

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME},{COUNTRY_CODE}&appid={API_KEY}"

# Data - get
response = requests.get(URL)
# Check status
if response.status_code == 200:
    data = response.json()
else:
    print(ERROR_MSG)

# Data - process
temp_min, temp_max, desc, rain = (
        data['main']['temp_min'],   # Temperature minimum
        data['main']['temp_max'],   # Temperature maximum
        data['weather'][0]['description'],  # Weather description
        data.get('rain', {}).get('1h', 0) # Chance of rain in the next hour
)

# Convertion
temp_min, temp_max = temp_min-KELVIN, temp_max-KELVIN
date = datetime.now().strftime('%Y-%m-%d')
time = datetime.now().strftime('%H:%M-%S')

# Display
print()
print(f"{'Weather Report':<20}{date:>10}")
print(f"{'Inquiry Time':<20}{time:>10}")
print("=" * 30)
print(f"{'LOCATION':<20}{CITY_NAME:>10}")
print(f"{'TEMP_LOW':<20}{temp_min:>8.2f}{'\u00B0C':>2}")
print(f"{'TEMP_HIGH':<20}{temp_max:>8.2f}{'\u00B0C':>2}")
print(f"{'TYPE':<10}{desc:>20}")
print(f"{'RAIN':<10}{rain:>20.2f}")
print()
