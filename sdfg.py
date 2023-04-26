import requests
import json
x = requests.get('https://home.openweathermap.org/api_keys')


api_key ='83f395ad9254deac0578dda8a658508d'
title = "mze"
temperatura = "30c"
url = f'https://home.openweathermap.org/api_keys?api_key={api_key}={title}&temperatura={temperatura}'
print(json.loads(x.text))
print(x.json())
print(x.status_code)
print(x.headers)
import sqlite3

conn = sqlite3.connect("weather")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  weather
(id INTEGER PRIMARY KEY AUTOINCREMENT,
weather(autoincrement),
title VARCHAR(),
temperature VARCHAR(),
""")

