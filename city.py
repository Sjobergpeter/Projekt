import json
import os
import ui
import pycountry
import requests

favorites = []
city = []

if os.path.isfile("favorites.json"):
    with open("favorites.json", "r") as f:
        favorites = json.load(f)

if os.path.isfile("city.json"):
    with open("city.json", "r") as f:
        city = json.load(f)


class City:
    # Konstruktor för nya objekt av klassen
    def __init__(self, city_name='', capital='', country='', population=0, latitude=0.0, longitude=0.0, input_city=''):
        self.city_name = city_name
        self.capital = capital
        self.country = country
        self.population = population
        self.latitude = latitude
        self.longitude = longitude
        self.input_city = input_city

    # Metod som startar UI och inmatning
    @staticmethod
    def city_start():
        ui.line()
        city_obj.input_city = input('Type a city name: > ')
        return city_obj.input_city

    # Metod för att hämta city information från API
    @staticmethod
    def get_city_api(self):
        city_in = city_obj.input_city
        url = f'https://api.api-ninjas.com/v1/city?name={city_in}'
        response = requests.get(url, headers={'X-Api-Key': '90lkoFCGJZryQ+TsMHlFTA==akrnZyMBsML9wyo9'})
        if response.status_code == requests.codes.ok:
            response_dict = json.loads(response.text)
            return response_dict
        else:
            print("Error:", response.status_code, response.text)

    # Metod för att hämta holiday information från API
    @staticmethod
    def get_holiday_api(self):
        city_dict = City.get_city_api(city_obj)
        try:
            country = city_dict[0]["country"]
        except IndexError:
            return 'No country found'
        year = '2023'
        holiday_name = 'major_holiday'
        api_url = 'https://api.api-ninjas.com/v1/holidays?country={}&year={}&type={}'.format(country, year,
                                                                                             holiday_name)
        response = requests.get(api_url, headers={'X-Api-Key': '90lkoFCGJZryQ+TsMHlFTA==akrnZyMBsML9wyo9'})
        if response.status_code == requests.codes.ok:
            response_dict = json.loads(response.text)
            return response_dict
        else:
            print("Error:", response.status_code, response.text)

    # Hämtar information från API och sparar i objektet
    def city_information(self):
        city_dict = City.get_city_api(city_obj)
        # Kontroll att city_dict innehåller en lista
        try:
            self.city_name = city_dict[0]["name"]
        except IndexError:
            return 'The city does not exist in the database'

        # Omvandlar capital true/false till text
        if city_dict[0]["is_capital"]:
            self.capital = 'is the capital city'
        else:
            self.capital = 'is not the capital city'

        # Gör om landskod till landsnamn. Finns inte koden i pycountry
        # returneras landskoden.
        try:
            c_code_to_name = pycountry.countries.get(alpha_2=city_dict[0]["country"])
            self.country = c_code_to_name.name
        except AttributeError:
            self.country = city_dict[0]["country"]

        self.population = city_dict[0]["population"]
        self.latitude = city_dict[0]["latitude"]
        self.longitude = city_dict[0]["longitude"]
        return self


# Skapar objektet som innehåller variabler om efterfrågad stad
city_obj = City()
counter = 1  # Räknare för om inmatning av stad ska startas
# Om en stad är sparad i city.json så läses den in
try:
    city_obj.input_city = city[0]
    # Ritar up UI för första körningen
    ui.clear()
    ui.line()
    ui.header("CITY DATA")
    ui.line()
except IndexError:
    counter = 0

while True:
    # UI
    ui.clear()
    ui.line()
    ui.header("CITY DATA")
    ui.line()
    # Om ingen stad finns sparad från huvudmenyn, skriv in en manuellt
    if counter < 1:
        # Startar gränsnittet och inmatning av stad
        City.city_start()
    counter = 0  # Räknaren nollställs så att manuell inmatning av stad sker nästa gång loopen körs

    # Hämtar data från API:erna city och holiday
    City.city_information(city_obj)
    holiday_info = City.get_holiday_api(city_obj)
    holiday_list = []

    # Resultatet från sökningen skrivs ut
    print(f'\n{city_obj.city_name} is a city in {city_obj.country}\nand {city_obj.capital}.')
    print(f'The population of {city_obj.city_name} is {city_obj.population:,}.')
    print(f'The location of the city is at \nlatitude {city_obj.latitude} and longitude {city_obj.longitude}.')

    ui.line()
    print(f'Press 1 to show major holidays in {city_obj.country}')
    print('Press 2 to search for another city')
    print('Press 3 to return to main menu')
    menu = input(':> ')

    if menu == '1':
        print(f'\n| Major holidays 2023 in {city_obj.country} |\n')

        # Loop som sparar dictionaryt i en lista efter datum och namn
        for i in holiday_info:
            holiday_list.append([i['date'], i['name']])

        # Helgdagslistan sorteras i datumordning och skrivs sedan ut
        holiday_list.sort(key=lambda item: item[0])
        for holiday in holiday_list:
            print(holiday[0], holiday[1])

    elif menu == '2':
        ui.line()
        ui.clear()
        continue
    elif menu == '3':
        break



