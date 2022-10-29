# TELECHARGER UNE IMAGE AVEC REQUESTS
#
# https://codeavecjonathan.com/res/papillon.jpg

import requests

response_photo = requests.get('https://codeavecjonathan.com/res/papillon.jpg')
if response_photo.status_code == 200:
    f = open("papillon.jpg", "wb")
    f.write(response_photo.content)
    f.close()
    print('Ecriture terminée')
else:
    print(f'ERREUR: {response_photo.status_code}')
