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
    # Funktion som kallar på vår api och sedan returnerar dictionaryn från api:en


def response_city(city_choice):
    api_url = f"https://api.api-ninjas.com/v1/airquality?city={city_choice}"
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})

    # Följande kontrollerar ifall staden finns i apin och fortsätter koden ifall status koden är 200 som returneras

    if response.status_code == 200:
        return True
    else:
        return False


def print_aqi(aqi_info):
    overall_aqi = int(aqi_info["overall_aqi"])

    # Vi tar info "overall air quality" från vår api och sedan skriver ut nedan ifall det är en bra eller
    # dålig luftkvalite.

    if overall_aqi <= 50:
        print(f"This city has an overall air quality index of {overall_aqi}, this is very good :D")
    elif overall_aqi < 100:
        print(f"This city has an overall air quality index of {overall_aqi}, this is a moderate level")
    elif overall_aqi < 150:
        print(f"This city has an overall air quality index of {overall_aqi}, these levels are unhealthy")
    elif overall_aqi < 200:
        print(f"This city has an overall air quality index of {overall_aqi}, these levels are very unhealthy")
    else:
        print("Please try to enter a city again")
    return


def print_aqi_list(aqi_info_dictionary):
    for info_name, info_value in aqi_info_dictionary.items():
        # i följande går vi igenenom i en loop vår key och value i dictionaryn
        # type funktionen jämnför datatypen info_value med dict om info_value är en dictionary fortsätter koden
        if type(info_value) is dict:
            aqi = info_value["aqi"]
            print(f"This is the overall aqi index levels: {aqi} for {info_name}")


def json_favorite():
    print("1 - Would you like to add a city to your favorites?")
    print("2 - Would you like to view your favorites?")
    json_choice = input("> ")

    # i följande nedanför lägger vi till namnet på den staden vi vill spara i våran json fil
    # som delas mellan alla våra moduler.

    if json_choice.lower() == "1":
        save_json = input("Enter the name of the city you would like to save: ")
        favorites.append(save_json)
        with open("favorites.json", "w") as file_write:
            json.dump(favorites, file_write)
        print("City Saved...")

    elif json_choice.lower() == "2":
        print("These are your favorites and their respective air quality scores: ")

        # i följande del av koden kan vi se alla våra favorites som sparats, sedan grävar vi fram aqi infon för alla
        # cities i favorites

        for cities in favorites:
            aqi_info = get_air_quality(cities)
            overall_aqi = int(aqi_info["overall_aqi"])
            print(f"- {cities} has an overall air quality of: {overall_aqi} ")
        print("-" * 30)
    else:
        input("This is not an option try again...")


def json_delete():

    # Funktion för att skriva in namnet på den staden man önskar ta bort från favorites
    for cities in favorites:
        print(f"- {cities}")
    delete_favorite = input("Enter the name of the city you want to delete from favorites: ")
    if delete_favorite in favorites:
        favorites.remove(delete_favorite)
        with open("favorites.json", "w") as file_write:
            json.dump(favorites, file_write)
    else:
        print("City not found in favorites.")


def get_city_choice(city):
    # Funktion för att kalla på vår huvudmenys input om vilken stad som api ska söka efter.
    global city_choice
    city_choice = city


def main():
    get_city_choice(city_choice)

    if response_city(city_choice): # kontrollerar ifall staden finns i API:n innan kodens körs.
        while True:
            print(city_choice.capitalize().center(30)) # Titel på programmet om vilken stad dom skrivit in.
            print("-" * 30)
            print("1 - air quality information")
            print("2 - specific air quality information")
            print("3 - add/view your favorites")
            print("4 - delete a favorite")
            print("5 - Exit")
            print("-" * 30)

            menu_choice = input("Choose an option: ")

            aqi_info = get_air_quality(city_choice) # sätter variabel på dictionaryn
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
                print("Going back to main menu")
                print("-" * 30)
                break
    else:
        print("This city does not exist...") # main körs ej ifall staden ej får 200 response ping.


if __name__ == "__main__":
    main()
