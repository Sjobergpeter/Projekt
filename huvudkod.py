import ui
import json

while True:
    city = input("Välj en stad ")
    with open("city.json", "w+") as f:
        f.write(json.dumps(city))

    ui.line()

    val = input("Välj en siffra ")  # Detta val ska sparas

    ui.line()
    if val == "1":
        import worldtime
    elif val == "2":
        import gruppuppgift
    elif val == "3":
        import weather
    elif val == "4":
        import city
