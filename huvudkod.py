import ui

while True:
    val = input("Välj en siffra ")
    ui.line()
    if val == "1":
        import worldtime
    elif val == "2":
        import gruppuppgift
    elif val == "3":
        import weather
    elif val == "4":    
        import city