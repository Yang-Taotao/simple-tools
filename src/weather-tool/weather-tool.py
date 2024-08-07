"""
Handles weather info
"""
# Imports
import json
import requests
from datetime import datetime
from typing import Optional

# Config
CITY_NAME = "Glasgow"
COUNTRY_CODE = "uk"
# Config - styling
STL_THICK = "=" * 40
STL_THIN = "-" * 40
# Config - Static
ERROR_MSG = "Failed to get weather data"
KELVIN = 273.15
with open('./env/config.json') as source:
    config = json.load(source)
API_KEY = config.get('API_KEY')

# Data - get


def weather_get(
        city_name: str = CITY_NAME,
        country_code: str = COUNTRY_CODE,
        api_key: str = API_KEY
    ) -> Optional[dict]:
    """Get weather data from web API

    Args:
        city_name (str): city name
        country_code (str): country code
        api_key (str): api access key

    Returns:
        Optional[dict]: Raw weather data dict if inquiry succeed
    """
    # Build URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={
        city_name},{country_code}&appid={api_key}"
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


def weather_process(data: dict) -> tuple:
    """Weather data processing module

    Args:
        data (dict): Raw weather data

    Returns:
        dt (tuple): Date and time strings
        temp (tuple): Min, max, feels temp, adjusted to celcius
        other (tuple): Weather type and descriptions strings
    """
    # Datetime
    dt = (
        datetime.fromtimestamp(data['dt']).strftime(
            '%Y-%m-%d'),  # Date - day
        datetime.fromtimestamp(data['dt']).strftime(
            '%H:%M:%S'),  # Date - time
    )
    # Temperature
    temp = (
        data['main']['temp_min'] - KELVIN,  # Min temp
        data['main']['temp_max'] - KELVIN,  # Max temp
        data['main']['feels_like'] - KELVIN,  # Feels like temp
    )
    # Other info
    other = (
        data['weather'][0]['main'],  # Weather type
        data['weather'][0]['description'],  # Weather description
    )
    # Returns
    return dt, temp, other


# Data - display


def weather_print(dt: tuple, temp: tuple, other: tuple) -> None:
    """Display weather results

    Args:
        dt (tuple): Date and time strings
        temp (tuple): Min, max, feels temp, adjusted to celcius
        other (tuple): Weather type and descriptions strings
    """
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
    # Process data
    dt, temp, other = weather_process(data)
    # Display
    weather_print(dt, temp, other)


# OPS
if __name__ == '__main__':
    weather_tool()
