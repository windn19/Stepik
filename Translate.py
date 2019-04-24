import requests

id_key = 'NmEwZjBjYjEtM2I2Yy00ZDExLTk0YTYtMWM1ZmRjZmM2YTJlOjFjMGI1NzNiN2M1ODQ2NzlhOWY4NDdjYTRjN2M3MmU4'

header = {'Authorization': f'Basic {id_key}'}

token = requests.post(url='https://developers.lingvolive.com/api/v1.1/authenticate', headers=header)
print(token.text)

header = {'Authorization': f'Bearer {token.text}'}

urlAPI = 'https://developers.lingvolive.com/api/v1/Translation'

par = {
    'text': 'Myth',
    'srcLang': 1033,
    'dstLang': 1049,
    'isCaseSensitive': True
}

res = requests.get(url='https://developers.lingvolive.com/api/v1/Translation', params=par, headers=header)
res.encoding = 'utf-8'
print(res.json())
