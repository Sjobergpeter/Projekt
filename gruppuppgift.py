import requests
import json

BOLD = '\033[1m'
END = '\033[0m'

while True:

    print("Enter a city name to learn about its weather or air quality:")
    city = input("> ").lower()

    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
    response_aqi = requests.get(api_url, headers={'X-Api-Key': 'Ma8t5bWqLp8Z1q0Lfz2Asw==q6kmQIVKHAsPeRIE'})
    aqi_dictionary = json.loads(response_aqi.text)
    air_quality = aqi_dictionary

    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response_weather = requests.get(api_url, headers={'X-Api-Key': 'Ma8t5bWqLp8Z1q0Lfz2Asw==q6kmQIVKHAsPeRIE'})
    weather_dictionary = json.loads(response_weather.text)
    weather_info = weather_dictionary

    print("Here is more info regarding your city")
    print("-" * 30)
    print("- Weather")
    print("- Air quality")
    choice = input("what would you like to know, weather or air quality?:  ").lower()

    if choice == "weather":
        for option in weather_info:
            print("*", option)

        weather_choice = input("what would you like to know more about: ").lower()

        for option in weather_info:
            if option.lower() == weather_choice:
                print(f"{option}: {weather_info[option]}")

    elif choice == "air quality":
        for option in air_quality:
            print("*", option)

        aqi_choice = input("what would you like to know more about: ").lower()

        for option in air_quality:
            if option.lower() == aqi_choice:
                for option_2 in air_quality[option]:
                    print(f"{option_2}: {air_quality[option][option_2]}")

    else:
        print("That is not an option...")
        print("Try again...")






    """print(weather_info["humidity"])

    print(f"{(BOLD + 'carbon monoxide' + END)} concentration levels for today:", air_quality["CO"]["concentration"])
    print(f"{(BOLD + 'carbon monoxide air quality index' + END)} levels for today:", air_quality["CO"]["aqi"])

    print(f"{(BOLD + 'partical matter 10' + END)} concentration level for today:", air_quality["PM10"]["concentration"])
    print(f"{(BOLD + 'partical matter air quality index' + END)} level for today:", air_quality["PM10"]["aqi"])

    print(f"{(BOLD + 'sulfur dioxide' + END)} concentration levels for today:", air_quality["SO2"]["concentration"])
    print(f"{(BOLD + 'sulfur dioxide air quality index' + END)} levels for today:", air_quality["SO2"]["aqi"])

    print(f"{(BOLD + 'ozone' + END)} concentration levels for today:", air_quality["O3"]["concentration"])
    print(f"{(BOLD + 'ozone air quality index' + END)} levels for today:", air_quality["O3"]["aqi"])

    print(f"{(BOLD + 'nitrogen dioxide' + END)} concentration levels for today:", air_quality["NO2"]["concentration"])
    print(f"{(BOLD + 'nitrogen dioxide quality index' + END)} levels for today:", air_quality["NO2"]["aqi"])

    print(f"{(BOLD + 'Overall air quality' + END)} levels for today:", air_quality["overall_aqi"])"""