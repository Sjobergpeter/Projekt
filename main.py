# Moduler som används
import ui
import os
import json
import worldtime
import Weather
import city
import aqi

favorites = []


# Funktion för att skriva ut favoriter
def check_favorites():
    # Skriver ut om ingen favorit finns i favorites.json
    if not favorites:
        ui.echo("No favorites saved yet" + "|".rjust(6))

    # Har en favorit hittats printar den ut alla
    else:
        ui.echo("Your current favorites:    |")
        for favorite in favorites:
            print(f"| {favorite:<{27}}|")


# Huvudprogrammet som körs
while True:
    # Läser av favoriter
    if os.path.isfile("favorites.json"):
        with open("favorites.json", "r") as f:
            favorites = json.load(f)

    # UI
    ui.clear()
    ui.line()
    ui.header("CITY PICKER 1.0")
    ui.line()

    # Hämtar funktion
    check_favorites()

    # Menyval
    ui.line()
    ui.echo("1 | Time and Date" + "|".rjust(11))
    ui.echo("2 | Air Quality Index" + "|".rjust(7))
    ui.echo("3 | Weather" + "|".rjust(17))
    ui.echo("4 | Info about the city" + "|".rjust(5))
    ui.echo("5 | Exit" + "|".rjust(20))
    ui.line()

    # Användaren väljer en stad
    ui.echo("Type a city or 5 to exit" + "|".rjust(4))
    choose_city = ui.prompt("")

    # Användaren kan välja att stänga programmet tidigt
    if choose_city == "5":
        ui.echo("You exited the program")
        exit()

    # Sparar valet i city.json
    with open("city.json", "w+") as f:
        f.write(json.dumps(choose_city))

    # Globala variablar som tilldelar choose_city
    worldtime.get_city_choice(choose_city)
    aqi.get_city_choice(choose_city)
    ui.line()

    # Användaren får välja info som ska tas fram
    val = ui.prompt("Choose a number in the menu")
    ui.line()

    # Startar worldtime.py
    if val == "1":
        worldtime.main(choose_city)

    # Startar aqi.py
    elif val == "2":
        aqi.main()

    # Startar weather.py
    elif val == "3":
        Weather.main()

    # Startar city.py
    elif val == "4":
        city.City.startprogram()

    # Stänger programmet
    elif val == "5":
        ui.echo("Thanks for using our program, exiting...")
        exit()

    # Felaktig inmatning
    else:
        ui.prompt("You did not enter a correct input, press enter to try again")
