import requests

cities = ['London', 'Шереметьево', 'Череповец', 'Полевской', 'New-York']

options = {
    'nTq': '',
    'lang': 'en'
}

for city in cities:
    url = f'http://wttr.in/{city}'
    options['lang'] = 'en' if ord(url[-1]) < 127 else 'ru'
    res = requests.get(url=url, params=options)
    res.encoding = 'utf-8'
    print(res.text)
