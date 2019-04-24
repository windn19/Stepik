import requests

urls = ['http://wttr.in/london?nTqu&lang=en',
       'http://wttr.in/Шереметьево?nTqu&lang=ru',
       'http://wttr.in/Череповец?nTqu&lang=ru']

for url in urls:
    res = requests.get(url)
    res.encoding = 'utf-8'
    print(res.text)