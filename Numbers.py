from requests import get
with open('input.txt', 'r', encoding='utf-8') as f:
    файл = f.readlines()
for line in файл:
    urlAPI = f'http://numbersapi.com/{line.strip()}/math'
    par = {
        'json': 'true'
    }

    res = get(url=urlAPI, params=par)
    data = res.json()
    print('Interesting' if data['found'] else 'Boring')
    print(data['text'])

