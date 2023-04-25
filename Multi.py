import requests

API_KEY = "2b8b0223d3a72847c10d8175a3606a9c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather']
    print(weather)
    temp = data["main"]["temp"]
    print(f"{temp}K")
    temp = float(temp)
    print (f"{temp - 273.15}C") 

else:
    print("Error has occured")

