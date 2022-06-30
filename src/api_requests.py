import requests
import json
import os

key = json.load(open(os.path.join('credentials.json')))
params = {'q': 'perlach', 'units': 'metric',
          'appid': key['appid']}
headers = {'Content-Type': 'application/json'}

# Aufgabe 1.1 - Längen- und Breitengrad meines Wohnortes
req_result = requests.get('https://api.openweathermap.org/data/2.5/weather',
                          params=params, headers=headers)

lon = req_result.json()['coord']['lon']
lat = req_result.json()['coord']['lat']

print('Längen- und Breitengrad meines Wohnortes: Perlach (München)')
print(f'Request status code: {req_result.status_code}')
print(f'Längengrad: {lon}')
print(f'Breitengrad: {lat}')
print()

# Aufgabe 1.2 - Wettervorhersage der nächsten 5 Tage

forecast = requests.get('https://api.openweathermap.org/data/2.5/forecast',
                        params=params, headers=headers)

forecast_list = forecast.json()['list']
print('Wettervorhersage der nächsten 5 Tage in Perlach (München)')
for item in forecast_list:
    print(f'Date: {item["dt_txt"]}')
    print(f'Temperature: {item["main"]["temp"]}')

# Aufgabe 1.3 - Historische Daten
# Zugang nur für Premium-Konto

hist_params = {'q': 'perlach, Bavaria, DE', 'type': 'hour',
               'start': '1369728000', 'end': '1369728000',
               'appid': key['appid']}
history = requests.get(
    'http://history.openweathermap.org/data/2.5/history/city', params=hist_params)

print(history.json())
