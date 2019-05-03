import requests

urlAPI ='https://api.artsy.net/api/tokens/xapp_token'
id_code = 'e0752d560ea7331546bf'
id_secret = '72639d9180ac68b478389dcf897c6408'
par = {
    'client_id': id_code,
    'client_secret': id_secret
}
atr = []
res = requests.post(url=urlAPI, data=par)
token = res.json()['token']
print(res)
with open('input.txt', 'r', encoding='utf-8') as f:
    for arts in f:
        header = {'X-Xapp-Token': token}
        res = requests.get(url=f'https://api.artsy.net/api/artists/{arts.rstrip()}', headers=header)
        res.encoding = 'utf-8'
        data = res.json()
        atr.append(tuple((data['birthday'], data['sortable_name'])))
for d, i in sorted(atr):
    print(i)
