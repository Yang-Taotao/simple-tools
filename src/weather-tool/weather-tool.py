"""
Handles weather info
"""
# Imports
import requests
from datetime import datetime

# Config
CITY_NAME = "Glasgow"
COUNTRY_CODE = "uk"
# Config - styling
STL_THICK = "=" * 40
STL_THIN = "-" * 40
# Config - Static
ERROR_MSG = "Failed to get weather data"
API_KEY = "dc927b3a3f59d84bc844ae1a74ef648f"
KELVIN = 273.15

# Data - get


def weather_get():
    """Get weather data from web API

    Returns:
        DATA (dict): weather data dict
    """
    # Build URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={
        CITY_NAME},{COUNTRY_CODE}&appid={API_KEY}"
    # Get data
    response = requests.get(url)
    # Check status
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(ERROR_MSG)
        return None


# Data - display


def weather_print(data):
    """Display weather results

    Args:
        data (dict): weather data dict
    """
    # Local repo
    # Datetime
    dt = (
        datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d'),
        datetime.fromtimestamp(data['dt']).strftime('%H:%M:%S'),
    )
    # Temperature
    temp = (
        data['main']['temp_min'] - KELVIN,
        data['main']['temp_max'] - KELVIN,
        data['main']['feels_like'] - KELVIN,
    )
    # Other info
    other = (
        data['weather'][0]['main'],
        data['weather'][0]['description'],
    )
    # Display
    print(f"{STL_THICK}")
    print(f"{'Weather Report':<20}{dt[0]:>20}")
    print(f"{STL_THIN}")
    print(f"{'Inquiry Time':<20}{dt[1]:>20}")
    print(f"{STL_THICK}")
    print(f"{'LOCATION':<20}{CITY_NAME:>20}")
    print(f"{'TEMP LOW':<20}{temp[0]:>18.2f}{'C':>2}")
    print(f"{'TEMP HIGH':<20}{temp[1]:>18.2f}{'C':>2}")
    print(f"{'TEMP FEEL':<20}{temp[2]:>18.2f}{'C':>2}")
    print(f"{STL_THIN}")
    print(f"{'WEATHER':<20}{other[0]:>20}")
    print(f"{'TYPE':<15}{other[1]:>25}")
    print(f"{STL_THICK}")


# Main func


def weather_tool():
    """
    Main weather tool func
    """
    # Get data
    data = weather_get()
    # Display
    weather_print(data)


# OPS
if __name__ == '__main__':
    weather_tool()
