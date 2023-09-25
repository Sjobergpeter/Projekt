import requests
import ui
import json
import os

# Test

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

    return {
        'city': city,
        'timezone': timezone,
        'datetime': datetime,
        'date': date,
        'time': time,
        'day_of_week': day_of_week,
        'hour': hour
    }


# Def för utskrift
def print_city_info(city_info):
    ui.line()
    ui.echo(f"The city {city_info['city']} is in the timezone of {city_info['timezone']}.")
    ui.echo(
        f"Today it is {city_info['day_of_week']} and the date is {city_info['date']} and the time is {city_info['time']}.")


# -- FUNKTIONER FÖR ALLA VAL -- #
# Val 1
def new_city():
    city_to_check = ui.prompt("Type a city")
    city_info = city_information(city_to_check)

    # Utskrift
    print_city_info(city_info)

    ui.line()
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


# Val 2
def compare_cities():
    # Välj två städer
    city1 = ui.prompt("Enter the first city")
    city2 = ui.prompt("Enter the second city")

    # Hämtar information om bägge städerna
    city1_info = city_information(city1)
    city2_info = city_information(city2)

    # För att ta fram endast positivt tal används abs
    # https://www.w3schools.com/python/ref_func_abs.asp
    time_difference = abs(int(city1_info['hour']) - int(city2_info['hour']))

    # Skriv ut tidsskillnaden i timmar
    ui.line()
    ui.echo(f"The time difference between {city1} and {city2} is {time_difference} hours")
    ui.line()
    ui.prompt("Press enter to continue")


# Val 3
def lookup_favorites():
    if not favorites:
        ui.prompt("You dont have any favorite cities saved, press enter to continue")

    else:
        for city in favorites:
            city_info = city_information(city)
            print_city_info(city_info)
        ui.line()
        ui.prompt("Press enter to continue")

        # Loopa igenom allt
        # Lägg in ny stad varje loop
        # Använd print_city_info för utskrift


# Val 4
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
        ui.prompt(f"{delete} doesnt exist in the favorites, press enter toc ontinue")


# -- PROGRAMMET -- #
while True:
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
    ui.echo("1 - Check a new city")
    ui.echo("2 - Compare cities")
    ui.echo("3 - Lookup your favorite/s")
    ui.echo("4 - Delete a favorite")
    ui.echo("5 - Exit")
    ui.line()

    # Användaren får ett val
    choice = ui.prompt("Type your choice")
    ui.line()

    # Kollar upp en ny stad
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
        input("You did not pick a correct choice, press enter to try again...")