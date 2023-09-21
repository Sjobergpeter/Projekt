import requests
import ui
import json
import os

favorites = []

if os.path.isfile("favorites.json"):
    with open("favorites.json", "r") as f:
        favorites = json.load(f)

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


def city_information(city):
    # Hämtar staden vi ska använda oss av
    city_info = get_api(city)

    # Hämtar allt vi behöver från dictionary
    timezone = city_info['timezone']
    datetime = city_info['datetime']
    date = format_date(city_info['year'], city_info['month'], city_info['day'])
    time = format_time(city_info['hour'], city_info['minute'])
    day_of_week = city_info['day_of_week']

    return {
        'city': city,
        'timezone': timezone,
        'datetime': datetime,
        'date': date,
        'time': time,
        'day_of_week': day_of_week
    }


# Def för utskrift
def print_city_info(city_info):
    ui.line()
    ui.echo(f"The city {city_info['city']} is in the timezone of {city_info['timezone']}.")
    ui.echo(
        f"Today it is {city_info['day_of_week']} and the date is {city_info['date']} and the time is {city_info['time']}.")
    ui.line()


# Val 1
def new_city():
    city_to_check = ui.prompt("Type a city")
    city_info = city_information(city_to_check)

    # Utskrift
    print_city_info(city_info)

    # Låter användaren spara sin favorit
    favorit = ui.prompt("Do you want to save this city as your favorite? (j/n)").lower()

    if favorit == "j":
        favorites.append(city_info['city'])

        with open("favorites.json", "w+") as f:
            json.dump(favorites, f)

        ui.prompt(f"You chose to save {city_to_check} as a favorite, press enter to continue")

    elif favorit == "n":
        ui.prompt(f"You chose to not save {city_to_check} as a favorite, press enter to continue")

    else:
        input("ERROR!")


# -- PROGRAMMET -- #
while True:
    # UI
    ui.clear()
    ui.line()
    ui.header("Datum/tider")
    ui.line()
    ui.echo("Din favoritstad:")

    if not favorites:
        ui.echo("No favorite is saved right now")

    for favorite in favorites:
        ui.echo(favorite)

    ui.line()
    ui.header("Choose an option")
    ui.echo("1 - Check a new city")
    ui.echo("2 - Compare cities")
    ui.echo("3 - Lookup your favorite")
    ui.echo("4 - Delete a favorite")

    # Användaren får ett val
    choice = ui.prompt("Type your choice")

    # Kollar upp en ny stad
    if choice == "1":
        new_city()
    elif choice == "2":
        print("")
    elif choice == "3":
        print("")
    else:
        input("You did not pick a correct choice, press enter to try again...")
