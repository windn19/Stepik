import requests

urlAPI = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'q': 'Polevskoy',
    'appid': '72cb7c83a8cbdfe4e3e4764feebb829f'

}

res = requests.get(urlAPI, params=params)
print(res.status_code)
print(res.headers)
print(res.text)