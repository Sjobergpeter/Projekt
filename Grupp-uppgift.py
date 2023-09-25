import requests
import json

BOLD = '\033[1m'
END = '\033[0m'


class WeatherInfo:

    def __init__(self):
        self.api_key = 'Ma8t5bWqLp8Z1q0Lfz2Asw==q6kmQIVKHAsPeRIE'

    def get_weather_info(self, city):
        api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'
        response_weather = requests.get(api_url, headers={'X-Api-Key': self.api_key})
        weather_dictionary = json.loads(response_weather.text)
        return weather_dictionary

    def get_air_quality_info(self, city):
        api_url = f'https://api.api-ninjas.com/v1/airquality?city={city}'
        response_aqi = requests.get(api_url, headers={'X-Api-Key': self.api_key})
        aqi_dictionary = json.loads(response_aqi.text)
        return aqi_dictionary

    def print_weather_info(self, weather_info):
        print("Here is more info regarding your city")
        print("-" * 30)
        print("- Weather")
        print("- Air quality")
        choice = input("What would you like to know, weather or air quality?: ").lower()

        if choice == "weather":
            self.print_options(weather_info)

        elif choice == "air quality":
            air_quality_info = self.get_air_quality_info(city)
            self.print_options(air_quality_info)

        else:
            print("That is not an option...")
            print("Try again...")

    def print_options(self, info):
        for option in info:
            print("*", option)

        choice = input("What would you like to know more about: ").lower()

        for option in info:
            if option.lower() == choice:
                print(f"{option}: {info[option]}")


if __name__ == "__main__":
    weather_info = WeatherInfo()

    while True:
        print("Enter a city name to learn about its weather or air quality:")
        city = input("> ").lower()

        weather_data = weather_info.get_weather_info(city)
        weather_info.print_weather_info(weather_data)
