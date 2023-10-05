import requests
import ui
import json
import os

favorites = []

# Dictionary för att ha alla månader i text istället
month_number = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}


# -- FUNKTIONER -- #
# Hämta API
def get_api(city):
    url = f'https://api.api-ninjas.com/v1/worldtime?city={city}'
    response = requests.get(url, headers={'X-Api-Key': 'P56lgPDrmRuinArO1ubksg==A0OfMd46O71uIjAv'})
    response_dict = json.loads(response.text)
    return response_dict


# Funktion för att kolla så city finns i API (felhantering)
# https://www.w3schools.com/python/ref_requests_response.asp
# 200 = ok
def city_exist(city):
    url = f'https://api.api-ninjas.com/v1/worldtime?city={city}'
    response = requests.get(url, headers={'X-Api-Key': 'P56lgPDrmRuinArO1ubksg==A0OfMd46O71uIjAv'})

    if response.status_code == 200:
        return True

    else:
        return False


# Behöver komma åt denna utanför funktionen, så använder global
# https://www.w3schools.com/python/python_variables_global.asp
def get_city_choice(city):
    global city_choice  # Använd global för att ändra den globala variabeln
    city_choice = city


# Formaterar datum till rätt format
def format_date(year, month, day):
    # Skapar month_in_letters, hämtar month
    # https://www.w3schools.com/python/ref_dictionary_get.asp
    month_in_letters = month_number.get(month)

    # Vill inte skriva tex "21/September" som datum så använder slicing [:3]
    # https://www.w3schools.com/python/python_strings_slicing.asp
    return f"{day}/{month_in_letters[:3]}-{year}"


# Formaterar klockan
def format_time(hour, minute):
    return f"{hour}:{minute}"


# Hämtar relevant info från staden
def city_information(city):
    city_info = get_api(city)

    # Hämtar allt vi behöver från dictionary
    timezone = city_info['timezone']
    datetime = city_info['datetime']
    date = format_date(city_info['year'], city_info['month'], city_info['day'])
    time = format_time(city_info['hour'], city_info['minute'])
    day_of_week = city_info['day_of_week']
    hour = city_info['hour']

    # Tilldelar detta
    return {
        'city': city,
        'timezone': timezone,
        'datetime': datetime,
        'date': date,
        'time': time,
        'day_of_week': day_of_week,
        'hour': hour
    }


# Funktion för utskrift
def print_city_info(city_info):
    ui.line()
    ui.echo(f"The city {city_info['city']} is in the timezone of {city_info['timezone']}.")
    ui.echo(
        f"Today it is {city_info['day_of_week']} and the date is {city_info['date']} and the time is {city_info['time']}.")


# -- FUNKTIONER FÖR ALLA VAL -- #
# Val 1 - Allmän info
def new_city():
    city_info = city_information(city_choice)

    # Utskrift
    print_city_info(city_info)

    ui.line()
    # Låter användaren spara sin favorit
    favorit = ui.prompt("Do you want to save this city as your favorite? (y/n)").lower()
    while True:
        if favorit == "y":

            favorites = []

            if os.path.isfile("favorites.json"):
                with open("favorites.json") as f:
                    favorites = json.load(f)

            favorites.append(city_info['city'])

            with open("favorites.json", "w+") as b:
                json.dump(favorites, b)

            ui.prompt(f"You chose to save {city_choice} as a favorite, press enter to continue")
            break

        elif favorit == "n":
            ui.prompt(f"You chose to not save {city_choice} as a favorite, press enter to continue")
            break

        else:
            favorit = ui.prompt("You need to type yes or no (y/n)")


# Val 2 - Jämföra städer
def compare_cities():
    # Välj en stad att jämföra mot
    city1 = ui.prompt("Choose a city to compare timezone with")
    # city2 = ui.prompt("Enter the second city")
    if city_exist(city1):
        # Hämtar information om bägge städerna
        city1_info = city_information(city1)
        city2_info = city_information(city_choice)

        # För att ta fram endast positivt tal används abs
        # https://www.w3schools.com/python/ref_func_abs.asp
        time_difference = abs(int(city1_info['hour']) - int(city2_info['hour']))

        # Skriv ut tidsskillnaden i timmar
        ui.line()
        ui.echo(f"The time difference between {city1} and {city_choice} is {time_difference} hours")
        ui.line()
        ui.prompt("Press enter to continue")
    else:
        ui.prompt(f"{city1} does not exist, press enter to continue")


# Val 3 - Kolla upp favoriter
def lookup_favorites():
    # Global så den ej endast nås lokalt
    global favorites

    # Hämtar och tilldelar favorites till favorites
    if os.path.isfile("favorites.json"):
        with open("favorites.json", "r") as f:
            favorites = json.load(f)

    if not favorites:
        ui.prompt("You dont have any favorite cities saved, press enter to continue")

    else:
        for city in favorites:
            city_info = city_information(city)
            print_city_info(city_info)
        ui.line()
        ui.prompt("Press enter to continue")


# Val 4 - Ta bort favoriter
def delete_favorites():
    if not favorites:
        ui.prompt("You dont have have favorite cities to remove, press enter to continue")
        return
    ui.header("Your favorites right now:")
    for n in favorites:
        ui.echo(n)

    delete = ui.prompt("What city do you want to remove")

    if delete in favorites:
        favorites.remove(delete)
        with open("favorites.json", "w+") as f:
            json.dump(favorites, f)

        ui.prompt(f"{delete} has been removed from favorites, press enter to continue")
    else:
        ui.prompt(f"{delete} doesnt exist in the favorites, press enter to continue")


# -- PROGRAMMET -- #
def main(city_choice):
    # Går in i while-loopen ifall API hittar staden
    if city_exist(city_choice):
        while True:

            favorites = []

            # Hämtar och tilldelar favorites till favorites
            if os.path.isfile("favorites.json"):
                with open("favorites.json", "r") as f:
                    favorites = json.load(f)

            # UI
            ui.clear()
            ui.line()
            ui.header("WORLD TIMES")
            ui.line()
            ui.echo("Your favorite places:")

            if not favorites:
                ui.echo("No favorite is saved right now")

            for favorite in favorites:
                ui.echo(favorite)

            ui.line()
            ui.header("Choose an option")
            ui.line()
            ui.echo("1 - Check time and date about the city")
            ui.echo("2 - Compare timezone with another city")
            ui.echo("3 - Lookup your favorite/s")
            ui.echo("4 - Delete a favorite")
            ui.echo("5 - Back to main menu")
            ui.line()

            # Användaren får ett val
            choice = ui.prompt("Type your choice")

            # Tilldelar valen till funktioner
            if choice == "1":
                new_city()
            elif choice == "2":
                compare_cities()
            elif choice == "3":
                lookup_favorites()
            elif choice == "4":
                delete_favorites()
            elif choice == "5":
                break
            else:
                ui.prompt("You did not pick a correct choice, press enter to try again...")
    else:
        ui.prompt("The city you entered doesnt exist, press enter to go back to the main menu")
