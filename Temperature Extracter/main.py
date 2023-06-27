import requests

city_name = "Kathmandu"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

with open("credentials.txt", "r") as f:
    api_key = f.read()

full_url = base_url + city_name + "&appid=" + api_key
# print(full_url)

response = requests.get(full_url)
data = response.json()
# print(data)

def kelvin_to_celsius(temp_kelvin):
    celsius = temp_kelvin - 273.15
    return celsius


city = data["name"]
temp_kelvin = data["main"]["temp"]
temp_celsius = kelvin_to_celsius(temp_kelvin)
formatted_temp_celsius = "{:.2f}".format(temp_celsius)

def output():

    print(city)
    print(formatted_temp_celsius + "°C")

output()



