# Imports
import unittest
from unittest.mock import patch, Mock
import json
from weather_tool.weather_tool import weather_get, weather_process, weather_print

# Tester


class TestWeatherFunc(unittest.TestCase):

    @patch('weather_tool.weather_tool.requests.get')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='{"API_KEY": "test_key"}')
    def test_weather_get(self, mock_open, mock_get):
        # Mock API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'dt': 0,
            'main': {
                'temp_min': 273.15,
                'temp_max': 373.15,
                'feels_like': 323.15,
            },
            'weather': [{
                'main': 'Raining',
                'description': 'Thunder and Lightening',
            }]
        }
        mock_get.return_value = mock_response

        # Call actual func
        result = weather_get()

        # Expectation
        expectation = {
            'dt': 0,
            'main': {
                'temp_min': 273.15,
                'temp_max': 373.15,
                'feels_like': 323.15,
            },
            'weather': [{
                'main': 'Raining',
                'description': 'Thunder and Lightening',
            }]
        }

        # Assess
        self.assertEqual(result, expectation)

    def test_weather_process(self):
        # Mock data
        data = {
            'dt': 0,
            'main': {
                'temp_min': 273.15,
                'temp_max': 373.15,
                'feels_like': 323.15,
            },
            'weather': [{
                'main': 'Raining',
                'description': 'Thunder and Lightening',
            }]
        }

        # Call actual func
        result = weather_process(data)

        # Expectation
        expectation = (
            ('1970-01-01', '00:00:00'),
            (0.00, 100.00, 50.00),
            ('Raining', 'Thunder and Lightening'),
        )

        # Assess
        self.assertEqual(result, expectation)

    @patch('builtins.print')
    def test_weather_print(self, mock_print):
        # Mock data
        dt, temp, other = (
            ('1970-01-01', '00:00:00'),
            (0.00, 100.00, 50.00),
            ('Raining', 'Thunder and Lightening'),
        )

        # Call actual func
        weather_print(dt, temp, other)

        # Check print
        mock_print.assert_any_call('=' * 40)
        mock_print.assert_any_call(f"{'Weather Report':<20}{dt[0]:>20}")
        mock_print.assert_any_call(f"{'Inquiry Time':<20}{dt[1]:>20}")
        mock_print.assert_any_call(f"{'LOCATION':<20}{'Glasgow':>20}")
        mock_print.assert_any_call(f"{'TEMP LOW':<20}{temp[0]:>18.2f}{'C':>2}")
        mock_print.assert_any_call(
            f"{'TEMP HIGH':<20}{temp[1]:>18.2f}{'C':>2}")
        mock_print.assert_any_call(
            f"{'TEMP FEEL':<20}{temp[2]:>18.2f}{'C':>2}")
        mock_print.assert_any_call(f"{'WEATHER':<20}{other[0]:>20}")
        mock_print.assert_any_call(f"{'TYPE':<15}{other[1]:>25}")
        mock_print.assert_any_call('=' * 40)


if __name__ == '__main__':
    unittest.main()
