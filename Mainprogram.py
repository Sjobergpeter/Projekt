import json
user_input = input("Enter a city >")
city = [user_input]
print (city)

with open('city.json', 'w') as myFile:
    myFile.write(json.dumps(city))