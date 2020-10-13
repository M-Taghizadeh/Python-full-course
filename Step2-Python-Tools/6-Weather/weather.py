import requests
import json

# url_api = "https://www.metaweather.com/api/location/search/?lattlong=35.6892,51.3890"
# response = requests.get(url_api)
# city_info = response.json()
# f = open("C:/Users/Zanis/Desktop/City_Info.json", "w+")
# json.dump(city_info, f)

city_id = "2251945"
url_api = "https://www.metaweather.com/api/location/"+ city_id +"/"
response = requests.get(url_api)
weather_info = response.json()

f = open("C:/Users/Zanis/Desktop/Weather_Info.json", "a+")
json.dump(weather_info, f)