# FAIRE DES APPELS RÉSEAU AVEC REQUESTS
#
# https://codeavecjonathan.com/res/programmation.txt
# https://codeavecjonathan.com/res/pizzas1.json
# https://codeavecjonathan.com/res/exemple.html

import requests
import json

# REST API
"""response = requests.get("https://codeavecjonathan.com/res/pizzas1.json")
if response.status_code == 200:
    response.encoding = "utf-8"
    print(response.text)
    pizzas = json.loads(response.text)
    print(pizzas)
    print(f"Nombre de pizzas: {len(pizzas)}")
else:
    print(f"ERREUR code: {response.status_code}")"""


response = requests.get("https://codeavecjonathan.com/res/exemple.html")
if response.status_code == 200:
    response.encoding = "utf-8"
    print(response.text)
else:
    print(f"ERREUR code: {response.status_code}")
