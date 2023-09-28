import ui
import json
import worldtime
# Lägg till weather och gruppuppgift
# import weather
# import gruppuppgift
# import city


# ändrar i koden


city_choice = ""

while True:
    ui.clear()
    ui.line()
    ui.header("")
    # Väljer stad samt lägger in den i city.json
    choose_city = ui.prompt("Pick a city")
    with open("city.json", "w+") as f:
        f.write(json.dumps(choose_city))

    # Global variabel i funktionen från worldtime
    worldtime.get_city_choice(choose_city)

    ui.line()

    val = ui.prompt("Pick a choice")

    ui.line()
    if val == "1":
        worldtime.main(choose_city)
    elif val == "2":
        import gruppuppgift
    elif val == "3":
        import weather
    elif val == "4":
        import city
