# Moduler som används
import ui
import os
import json
import worldtime
import Weather
import city
import aqi

def check_favorites():
    if not favorites:
        ui.echo("No favorites saved yet")

    else:
        for favorite in favorites:
            ui.echo(favorite)

favorites = []

if os.path.isfile("favorites.json"):
    with open("favorites.json", "r") as f:
        favorites = json.load(f)

# Huvudprogrammet som körs
while True:

    # UI
    ui.clear()
    ui.line()
    ui.header("CITY PICKER 1.0")
    ui.line()

    check_favorites()

    ui.line()
    ui.echo("1 | Time and Date" + "|".rjust(11))
    ui.echo("2 | Air Quality Index" + "|".rjust(7))
    ui.echo("3 | Weather" + "|".rjust(17))
    ui.echo("4 | Info about the city" + "|".rjust(5))
    ui.echo("5 | Exit" + "|".rjust(20))
    ui.line()

    # Användaren väljer en stad
    choose_city = ui.prompt("Pick a city")

    # Sparar valet i city.json
    with open("city.json", "w+") as f:
        f.write(json.dumps(choose_city))

    # Global variabel som tilldelar choose_city till variabel i worldtime.py
    worldtime.get_city_choice(choose_city)
    aqi.get_air_quality(choose_city)
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