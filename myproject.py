import requests


response = requests.get('https://api.github.com/users/annachelondaeva')

print(response.text)
