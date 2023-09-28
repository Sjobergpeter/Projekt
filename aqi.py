import requests
import os
import json

API_KEY = "Ma8t5bWqLp8Z1q0Lfz2Asw==q6kmQIVKHAsPeRIE"

favorites = []

if os.path.isfile("favorites.json"):
    with open("favorites.json", "r") as file_read:
        favorites = json.load(file_read)


def get_air_quality(city_choice):
    api_url = f"https://api.api-ninjas.com/v1/airquality?city={city_choice}"
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})
    aqi_dictionary = json.loads(response.text)
    return aqi_dictionary


def print_aqi(aqi_info):
    overall_aqi = int(aqi_info["overall_aqi"])
    if overall_aqi <= 50:
        print(f"This city has an over all air quality index of {overall_aqi}, this is very good :D")
    elif overall_aqi < 100:
        print(f"This city has an over all air quality index of {overall_aqi}, this is a moderate level")
    elif overall_aqi < 150:
        print(f"This city has an over all air quality index of {overall_aqi}, these levels are unhealthy")
    elif overall_aqi < 200:
        print(f"This city has an over all air quality index of {overall_aqi}, these levels are very unhealthy")
    else:
        print("Please try to enter a city again")
    return


def print_aqi_list(aqi_info_dictionary):
    for info_name, info_value in aqi_info_dictionary.items():
        if type(info_value) is dict:
            print("", info_name)
            aqi = info_value["aqi"]
            print(f"This is the overall aqi index: {aqi}")


def json_favorite():
    save_json = input("Enter the name of the city you would like to save: ")
    favorites.append(save_json)
    with open("favorites.json", "w") as file_write:
        json.dump(favorites, file_write)


def json_delete():
    delete_favorite = input("Enter the name of the city you want to delete from favorites: ")
    if delete_favorite in favorites:
        favorites.remove(delete_favorite)
        with open("favorites.json", "w") as file_write:
            json.dump(favorites, file_write)
    else:
        print("City not found in favorites.")


def get_city_choice(city):
    global city_choice
    city_choice = city


def main():
    while True:

        """city_choice = input("Enter a city name: ").lower()"""
        print("-" * 30)

        print("1 - air quality information")
        print("2 - specific air quality information")
        print("3 - save your favorites")
        print("4 - delete a favorite")
        print("5 - Exit")
        print("-" * 30)
        menu_choice = input("Choose an option: ")

        aqi_info = get_air_quality(city_choice)
        print("-" * 30)

        if menu_choice == "1":
            print_aqi(aqi_info)
        elif menu_choice == "2":
            print_aqi_list(aqi_info)
        elif menu_choice == "3":
            json_favorite()
        elif menu_choice == "4":
            json_delete()
        elif menu_choice == "5":
            break


if __name__ == "__main__":
    main()
