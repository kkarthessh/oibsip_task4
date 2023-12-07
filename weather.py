import requests
import json
def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
def display_weather(data):
    if data:
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather Conditions: {data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather data.")
if __name__ == "__main__":
    api_key = "8259f605bb738e6dbeff1b7d324637d3"
    location = input("Enter city name or zip code: ")
    weather_data = get_weather(api_key, location)
    if weather_data:
        display_weather(weather_data)