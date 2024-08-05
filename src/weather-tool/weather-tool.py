"""
Handles weather info
"""
# Imports
import requests
from datetime import datetime

# Config
CITY_NAME = "Glasgow"
COUNTRY_CODE = "uk"

# Config - Static
ERROR_MSG = "Failed to get weather data"
API_KEY = "dc927b3a3f59d84bc844ae1a74ef648f"
KELVIN = 273.15

# Data - get


def weather_get():
    # Build URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME},{COUNTRY_CODE}&appid={API_KEY}"
    # Get data
    response = requests.get(url)
    # Check status
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(ERROR_MSG)
        return None


# Data - process


def weather_read(data):
    # Read weather data
    temp_min, temp_max, desc, rain = (
        data['main']['temp_min'],   # Temperature minimum
        data['main']['temp_max'],   # Temperature maximum
        data['weather'][0]['description'],  # Weather description
        data.get('rain', {}).get('1h', 0) # Chance of rain in the next hour
    )
    return temp_min, temp_max, desc, rain


def weather_print(temp_min, temp_max, desc, rain):
    # Get current date and time
    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M-%S')
    # Display
    print("=" * 30)
    print(f"{'Weather Report':<20}{date:>10}")
    print("-" * 30)
    print(f"{'Inquiry Time':<20}{time:>10}")
    print("-" * 30)
    print(f"{'LOCATION':<10}{CITY_NAME:>20}")
    print(f"{'LOW':<5}{temp_min:>22.2f}{'\u00B0C':>3}")
    print(f"{'HIGH':<5}{temp_max:>22.2f}{'\u00B0C':>3}")
    print(f"{'TYPE':<5}{desc:>25}")
    print(f"{'RAIN':<5}{rain:>25.2f}")
    print("=" * 30)


def weather_tool():
    # Get data
    data = weather_get()
    temp_min, temp_max, desc, rain = weather_read(data)
    # Convertion
    temp_min, temp_max = temp_min-KELVIN, temp_max-KELVIN
    # Display
    weather_print(temp_min, temp_max, desc, rain)
    

# OPS
if __name__ == '__main__':
    weather_tool()
