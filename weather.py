import requests
import json
import time

class OpenWeatherMapClient:
    def __init__(self):
        self.api_key = "2731ebffb8c21f0746d96c046462a7d7"

    def get_weather(self, city):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}")
        time.sleep(5)        
        return response.text


# Dependency injecting the client instance through the init method.
class WeatherData:
    def __init__(self, client):
        self.client = client

    def get_temperature(self, city):
        result = self.client.get_weather(city)
        oResult = json.loads(result)

        return oResult["main"]["temp"]
    
    def get_humidity(self, city):
        result = self.client.get_weather(city)
        oResult = json.loads(result)

        return oResult["main"]["humidity"]



