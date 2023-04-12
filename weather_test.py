from pytest_mock import mocker
from weather import *

def test_get_temperature(mocker):
    mock_client = mocker.MagicMock()
    
    mock_client.configure_mock(
        **{
            "get_weather.return_value": """ {"main": { "temp": 50.5 } } """,
        })
    
    data = WeatherData(mock_client)

    result = data.get_temperature("New York")

    assert type(result) is float, "get_temperature result is not a float"

def test_get_humidity(mocker):
    mock_client = mocker.MagicMock()
    
    mock_client.configure_mock(
        **{
            "get_weather.return_value": """ {"main": { "humidity": 999 } } """,
        })
    
    data = WeatherData(mock_client)

    result = data.get_humidity("New York")

    assert type(result) is int, "get_humidity result is not a float"

