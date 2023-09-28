import requests
import datetime
import json
import os

def main():
    def weather_cloud():
        coverage = ""
        
        if weather['cloud_pct'] > 30 and weather['cloud_pct'] < 60:
            coverage = "partially cloudy"
        elif weather['cloud_pct'] >= 60:
            coverage = "cloudy"
        else:
            coverage = "sunny"
        print (f"It's {coverage} in {city.capitalize()} with a cloud coverage of {weather['cloud_pct']}%")

    def weather_temp():
        if weather['temp'] != weather["feels_like"]:
            print (f"the temperature is currently at {weather['temp']}°C but feels like {weather['feels_like']} °C")
        else: 
            print (f"the temperature is currently at {weather['temp']}°C")
        print (f"The temperature range today will be between {weather['min_temp']}°C and {weather['max_temp']}°C")

    def weather_humid():
        print (f"Humidity level is at {weather['humidity']}%")

    def weather_wind():
        degrees = weather["wind_degrees"]
        cardinals = ["Northern", "Northeastern", "Eastern", "Southeastern", "Southern", "Southwestern", "Western", "Northwestern", "Northern"]
        cardinal = cardinals[round(degrees / 45)]
        print (F"There's a {cardinal} wind at {weather['wind_speed']} meters per second")

    def weather_sun():
        sunrise_timestamp = weather['sunrise']
        sunset_timestamp = weather['sunset']

        sunrise_datetime = datetime.datetime.utcfromtimestamp(sunrise_timestamp)
        sunset_datetime = datetime.datetime.utcfromtimestamp(sunset_timestamp)

        print(f"Today the sun rises in {city.capitalize()} at {sunrise_datetime.strftime('%H:%M')} (UTC) and sets at {sunset_datetime.strftime('%H:%M')}")
    # Gets the chosen city from city.json
    main_input = ""
    with open ("city.json", "r") as myFile:
        main_input = myFile.read()
        main_input = json.loads(main_input)
    city = main_input

    # city = input("Enter a city: ")
    api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'
    response = requests.get(api_url, headers={'X-Api-Key': 'dYoSBiEQ2LdY439GrifdSw==7OgS2qGCvv1GiXs8'})

    if response.status_code != requests.codes.ok:
        print("Could not fetch the weather from", city)
        input("Press Enter to continue")

    if response.status_code == requests.codes.ok:
        weather = response.json()
        while True:  
            os.system("cls") if os.name == "nt" else os.system("clear")

            print(".:     Weather Analyzer     :.")
            print("-" * 30)
            print("""| 1 | Cloud
    | 2 | Temperature
    | 3 | Wind
    | 4 | Humidity
    | 5 | Sun forecast
    | 6 | All of the above
    | 7 | Exit Weather Analyzer""")
            print ("-" * 30)
            print("Type the number for the alternative")
            user_input = input("you wish to know more about: ")
            os.system("cls") if os.name == "nt" else os.system("clear")
            print(".:     Weather Analyzer     :.")
            print("-" * 30)

            if user_input == "1":
                weather_cloud()
                input ("Press Enter to continue")
                continue
            elif user_input == "2":
                weather_temp()
                input ("Press Enter to continue")
                continue
            elif user_input == "3":
                weather_wind()
                input ("Press Enter to continue")
                continue
            elif user_input == "4":
                weather_humid()
                input ("Press Enter to continue")
                continue
            elif user_input == "5":
                weather_sun()
                input ("Press Enter to continue")
                continue
            elif user_input == "6":
                weather_cloud()
                print("-" * 30)
                weather_temp()
                print("-" * 30)
                weather_wind()
                print("-" * 30)
                weather_humid()
                print("-" * 30)
                weather_sun()
                print("-" * 30)
                input ("Press Enter to continue")
                continue
            elif user_input == "6":
                weather_temp()
                input ("Press Enter to continue")
                continue
            elif user_input == "7":
                break
            else:
                print("Invalid input")
                input("Press Enter to continue")
                continue

    # {"cloud_pct": 75, "temp": 17, "feels_like": 16, "humidity": 70, "min_temp": 14, "max_temp": 18, "wind_speed": 2.06, "wind_degrees": 0, "sunrise": 1695275057, "sunset": 1695319397}
