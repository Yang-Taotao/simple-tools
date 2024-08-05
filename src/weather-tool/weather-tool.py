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
    """Get weather data from web API

    Returns:
        data (dict): weather data dict
    """
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
    """Read weather data

    Args:
        data (dict): weather data dict

    Returns:
        temp_min (float): min temperature
        temp_max (float): max temperature
        desc (str): weather description
        rain (float): rain amount
    """
    # Read weather data
    temp_min, temp_max, desc, rain = (
        data['main']['temp_min'],   # Temperature minimum
        data['main']['temp_max'],   # Temperature maximum
        data['weather'][0]['description'],  # Weather description
        data.get('rain', {}).get('1h', 0)  # Rain in the last hour
    )
    # Convertion
    temp_min, temp_max = temp_min-KELVIN, temp_max-KELVIN
    # Func return
    return temp_min, temp_max, desc, rain


# Data - display


def weather_print(temp_min, temp_max, desc, rain):
    """Display weather results

    Args:
        temp_min (float): converted min temperature
        temp_max (float): converted max temperature
        desc (str): weather description
        rain (float): rain amount
    """
    # Get current date and time
    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M:%S')
    # Display
    print("=" * 30)
    print(f"{'Weather Report':<20}{date:>10}")
    print("-" * 30)
    print(f"{'Inquiry Time':<20}{time:>10}")
    print("-" * 30)
    print(f"{'LOCATION':<10}{CITY_NAME:>20}")
    print(f"{'TEMP LOW':<10}{temp_min:>18.2f}{'C':>2}")
    print(f"{'TEMP HIGH':<10}{temp_max:>18.2f}{'C':>2}")
    print(f"{'TYPE':<5}{desc:>25}")
    print(f"{'RAIN 1H':<10}{rain:>20.2f}")
    print("=" * 30)


# Main func


def weather_tool():
    """
    Main weather tool func
    """
    # Get data
    data = weather_get()
    # Display
    weather_print(*weather_read(data))


# OPS
if __name__ == '__main__':
    weather_tool()
