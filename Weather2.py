import requests

urls = ['http://wttr.in/london',
       'http://wttr.in/Первоуральск',
       'http://wttr.in/Череповец']

par = {
    'nTqu': '',
    'lang': 'en'
}

for url in urls:
    par['lang'] = 'en' if ord(url[-1]) < 127 else 'ru'
    res = requests.get(url, params=par)
    res.encoding = 'utf-8'
    print(res.url)
    print(res.text)
