import json
import requests

ui_width = 30

url = 'http://worldtimeapi.org/api/timezone/'
url_ip = 'http://worldtimeapi.org/api/ip'

response_ip = requests.get(url_ip)
response_ip_dictionary = json.loads(response_ip.text)

timezone = response_ip_dictionary['timezone']

response = requests.get(url + timezone)
response_dictionary = json.loads(response.text)

print("-" * ui_width)
print("| Information om din plats:", " |")
print("-" * ui_width)

for n in response_dictionary:
    print("|", n, ':', response_dictionary[n])
print("-" * ui_width)















'''
# Listar alla tillgängliga tidszoner
for i in response_dictionary:
    print(i)

# Skriv in namnet på tidszonen
print('.: Choose a time zone :.')
timezone = input('> ')

# Skickar förfrågan på tidszonen till servern
response = requests.get(url + timezone)
response_dictionary = json.loads(response.text)

# Innehållet från förfrågan skrivs ut
for i in response_dictionary:
    print(i, ':', response_dictionary[i])

# http://worldtimeapi.org/api/ip
'''