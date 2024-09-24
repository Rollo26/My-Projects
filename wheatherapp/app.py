import requests

api_key = 'a5460625ef87956476982241737185df'

user_data = input("Enter City: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_data}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temperature = round(weather_data.json()['main']['temp'])
print(f"The weather in {user_data} is: {weather}")
print(f"The temperature in {user_data} is: {temperature} Degrees Fahrenheit")