import requests
import json
from pprint import pprint

url = "https://pokeapi.co/api/v2/pokemon/"

while True:
    pokemon = input("Which pokemon would you like to look up: ")
    response = requests.get(url + pokemon.lower())
    data = response.json()
    print("Pokemon Index Number: " + str(data['order']))
    print("Pokemon Name: " + data['name'])
    for type in data['types']:
        print("Pokemon Type: " + type['type']['name'])
