import ui
import json
import worldtime

city_choice = ""

while True:
    ui.clear()

    # Väljer stad samt lägger in den i city.json
    city = ui.prompt("Välj en stad ")
    with open("city.json", "w+") as f:
        f.write(json.dumps(city))

    # Global variabel i funktionen från worldtime
    worldtime.get_city_choice(city)

    ui.line()

    val = ui.prompt("Välj en siffra ")

    ui.line()
    if val == "1":
        worldtime.main(city)
    elif val == "2":
        import gruppuppgift
    elif val == "3":
        import weather
    elif val == "4":
        import city
