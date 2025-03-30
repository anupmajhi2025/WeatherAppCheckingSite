import requests
from dotenv import load_dotenv
import os
import json
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv("API_KEY")
@dataclass
class WeatherData:
    name : str
    region : str
    country : str
    temp_c : float
    temp_f : float
    icon: str
    

def get_lan_log(city_name,API_key):
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_key}&q={city_name}&aqi=no").json()
    data = WeatherData(
        name     = response.get("location").get("name"),
        region   = response.get("location").get("region"),
        country  = response.get("location").get("country"),
        
        temp_c   = response.get("current").get("temp_c"),
        temp_f   = response.get("current").get("temp_f"),
        icon     = response.get("current").get("condition").get("icon")
    )
    
    
    return data

def main(city_name):
    WeatherData = get_lan_log(city_name, api_key)
    return WeatherData
    
    
if __name__ == "__main__":
   print(get_lan_log("India", api_key))    

