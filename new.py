import requests
from colorama import Fore, Back, Style, init
import pyfiglet

from dotenv import load_dotenv
import os

load_dotenv()
init()
text = pyfiglet.figlet_format("WEATHER APP")
print(text)
print(Fore.GREEN + "Welcome to the Weather App!")
print(Fore.RED + "Please enter the city name to get the current weather information.")
input_city = input(Style.BRIGHT + "Enter the city name: ")

print(Style.BRIGHT + "This is the Results:")

API_KEY = os.getenv("API_KEY")
city = input_city

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

response = requests.get(url)

data = response.json()

print(Fore.GREEN + str(data['current']['temp_c']) + "°C")
print(Fore.BLUE + str(data['current']['humidity']) + "%")