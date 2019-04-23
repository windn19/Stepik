import requests

urlAPI = 'http://api.openweathermap.org/data/2.5/weather'
city = input("City: ")
params = {
    'q': city,
    'appid': '72cb7c83a8cbdfe4e3e4764feebb829f',
    'units': 'metric',
    'lang': 'ru'
}

res = requests.get(urlAPI, params=params)
print(res.status_code)
print(res.headers['Content-Type'])
print(res.text)
data = res.json()
print()
print(data['main']['temp'])
temp = data['main']['temp']
print(f'current temperature in {city} is {temp}')
