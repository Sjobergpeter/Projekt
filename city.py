import json
import os
import ui
import pycountry
import requests

# Lista som sparar favoritstäder
favorites = []


# Klassen hanterar all information som reurneras från API:erna
class City:

    # Konstruktor för nya objekt av klassen
    def __init__(self, city_name='', capital='', country='', population=0, latitude=0.0, longitude=0.0, input_city='',
                 country_code=''):
        self.city_name = city_name
        self.capital = capital
        self.country = country
        self.country_code = country_code
        self.population = population
        self.latitude = latitude
        self.longitude = longitude
        self.input_city = input_city

    def get_city_api(self):
        """
        Hämtar city information från API

        Args:
            self: Ett City objekt

        Returns:
            En lista med flera dictionarys
        """

        city_in = self.input_city
        url = f'https://api.api-ninjas.com/v1/city?name={city_in}'
        response = requests.get(url, headers={'X-Api-Key': '90lkoFCGJZryQ+TsMHlFTA==akrnZyMBsML9wyo9'})
        if response.status_code == requests.codes.ok:
            response_dict = json.loads(response.text)
            return response_dict
        else:
            print("Error:", response.status_code, response.text)
            return

    def get_holiday_api(self):
        """
           Hämtar holiday information från API

           Args:
               self: Ett City objekt

           Returns:
               En lista med ett dictionary per helgdag
        """

        country = self.country_code
        year = '2023'
        holiday_name = 'major_holiday'
        api_url = f'https://api.api-ninjas.com/v1/holidays?country={country}&year={year}&type={holiday_name}'
        response = requests.get(api_url, headers={'X-Api-Key': '90lkoFCGJZryQ+TsMHlFTA==akrnZyMBsML9wyo9'})
        if response.status_code == requests.codes.ok:
            response_dict = json.loads(response.text)
            return response_dict
        else:
            print("Error:", response.status_code, response.text)

    def city_information(self):
        """
         Hämtar information från get_city_api och sparar i objektet

         Args:
            self: Ett City objekt

        Returns:
             Ett City objekt med alla attribut tilldelade
        """
        city_dict = City.get_city_api(city_obj)
        # Kontroll att city_dict innehåller en lista
        try:
            self.city_name = city_dict[0]["name"]
        except IndexError:
            print('The city does not exist in the database')
            return
        except Exception as e:
            # Hanterar alla andra undantag
            print("An unknown exception occured:", e)
            return

        # Omvandlar capital true/false till text
        if city_dict[0]["is_capital"]:
            self.capital = 'is the capital city'
        else:
            self.capital = 'is not the capital city'

        # Gör om landskod till landsnamn. Finns inte koden i pycountry
        # returneras landskoden.
        try:
            c_code_to_name = pycountry.countries.get(alpha_2=city_dict[0]["country"])
            self.country = c_code_to_name.name  # Landsnamnet sparas
            self.country_code = city_dict[0]["country"]
        except AttributeError:
            self.country = city_dict[0]["country"]

        # Kontroll om API ej har tilldelat alla värden korrekt
        try:
            self.population = city_dict[0]["population"]
            self.latitude = city_dict[0]["latitude"]
            self.longitude = city_dict[0]["longitude"]
            return self
        except KeyError:
            print('Not found')
            return self

    # Metoder som hanterar favoriter
    @staticmethod
    def load_favorites():
        global favorites
        # Fil för favoritstäder läses in
        if os.path.isfile("favorites.json"):
            with open("favorites.json", "r") as f:
                favorites = json.load(f)

    @staticmethod
    def your_favorite():
        if not favorites:
            ui.echo("No favorite cities saved.")
            ui.prompt("Press enter to continue")

        else:
            for i in favorites:
                # Favoritstaden sätts till .input_city
                city_obj.input_city = i
                # Cityobjektet skickas till API
                City.city_information(city_obj)
                print(f'{i} is a city in {city_obj.country}\nThe population is {city_obj.population:,}.')
                ui.line()
            ui.prompt("Press enter to continue")

    # Metod för att ta bort favoriter
    @staticmethod
    def delete_favorites():
        if not favorites:
            ui.echo("No favorite cities to remove!")
            ui.prompt("Press enter to continue")
            return
        ui.header("Your favorites right now:")
        for n in favorites:
            ui.echo(n)

        delete = ui.prompt("What city do you want to remove?")

        if delete in favorites:
            favorites.remove(delete)
            with open("favorites.json", "w") as file:
                json.dump(favorites, file)

            ui.echo(f"{delete} has been removed from favorites.")
            ui.prompt("Press enter to continue")
        else:
            ui.echo(f"{delete} doesn't exist in favorites.")
            ui.prompt("Press enter to continue")

    # Metod som startar sökning av stad, utskrift av city info, helgdagar & spara favorit
    @staticmethod
    def city_start():
        city_obj.input_city = input('Type a city name: > ')
        # Hämtar data från API:erna city och holiday
        City.city_information(city_obj)
        holiday_info = City.get_holiday_api(city_obj)
        holiday_list = []

        # Resultatet från sökningen skrivs ut
        print(f'\n{city_obj.city_name} is a city in {city_obj.country}\nand {city_obj.capital}.')
        print(f'The population of {city_obj.city_name} \nis {city_obj.population:,}.')
        print(f'The location of the city is at \nlatitude {city_obj.latitude} and\nlongitude {city_obj.longitude}.')
        ui.line()
        holidays = ui.prompt(f'Would you like to see major\nholidays in {city_obj.country} (yes/no)?').lower()
        ui.line()
        # Om användaren vill visa holidays körs denna kod
        if holidays == 'yes':
            print(f'\n| Major holidays 2023 in {city_obj.country} |\n')

            try:
                # Loop som sparar dictionaryt i en lista efter datum och namn
                for i in holiday_info:
                    holiday_list.append([i['date'], i['name']])

                # Helgdagslistan sorteras i datumordning och skrivs sedan ut
                holiday_list.sort(key=lambda item: item[0])
                for holiday in holiday_list:
                    print(holiday[0], holiday[1])

            except TypeError:
                print('Something went wrong')
            except Exception as e:
                # Hanterar alla andra undantag
                print("An unknown exception occured:", e)

        ui.line()
        # Låter användaren spara sin favorit
        favorit = ui.prompt("Do you want to save this\n| city as your favorite? (y/n)").lower()

        if favorit == "y":
            favorites.append(city_obj.city_name)

            with open("favorites.json", "w+") as b:
                json.dump(favorites, b)

            ui.echo(f"{city_obj.city_name} saved as a favorite.")
            ui.prompt("Press enter to continue")

        elif favorit == "n":

            ui.echo(f"{city_obj.city_name} not saved as a favorite.")
            ui.prompt("Press enter to continue")

        else:
            input("ERROR!")

    # Metod som anropas från huvudmenyn och returnerar city information.
    # Körs första gången sedan körs City.main() metoden
    @staticmethod
    def startprogram():
        # Om en stad är sparad i city.json så läses den in vid start
        if os.path.isfile("city.json"):
            with open("city.json", "r") as file:
                city_in = json.load(file)

        # Kontroll att det finns något sparat i city.json
        if len(city_in) > 0:
            city_obj.input_city = city_in
            # Ritar up UI för första körningen
            City.city_information(city_obj)
            ui.clear()
            ui.line()
            ui.header("CITY DATA")
            ui.line()
            # Resultatet från sökningen skrivs ut
            print(f'\n{city_obj.city_name} is a city in {city_obj.country}\nand {city_obj.capital}.')
            print(f'The population of {city_obj.city_name} \nis {city_obj.population:,}.')
            print(f'The location of the city is at \nlatitude {city_obj.latitude} and longitude\n{city_obj.longitude}.')
            ui.line()
            input('> Press Enter to continue\n')
            City.main()
        else:
            print('Error, the city is not in the database')
            input('> Press Enter to continue\n')
            # Huvudmetoden anropas
            City.main()

    # - Huvudprogrammet startar -
    @staticmethod
    def main():
        # Huvudprogrammets menyfunktion
        while True:
            # Favoritstäder läses in
            City.load_favorites()
            # UI utskrift
            ui.clear()
            ui.line()
            ui.header("CITY DATA")
            ui.line()
            ui.echo("Your favorite places:")
            if not favorites:
                ui.echo("No favorite is saved right now")

            for favorite in favorites:
                ui.echo(favorite)

            ui.line()
            ui.line()
            ui.header("Choose an option")
            ui.line()
            print('1 | Search for a city')
            print('2 | Lookup your favorite/s')
            print('3 | Delete a favorite')
            print('4 | return to main menu')
            ui.line()
            menu = input(':> ')

            # Inmatning av menyval
            if menu == '1':
                # Sökmetoden anropas
                City.city_start()

            elif menu == '2':
                # Favoritmetoden anropas
                City.your_favorite()

            elif menu == '3':
                # Ta bort favorit anropas
                City.delete_favorites()

            elif menu == '4':
                # Avsluta och återgå till huvudmenyn
                break

            else:
                continue


# Skapar objektet med attribut om efterfrågad stad
city_obj = City()

# Om programmet körs fristående startas main metoden härifrån
if __name__ == "__main__":
    City.main()
