from requests import post, get



def short_link(links, token):
    url = 'https://api-ssl.bitly.com/v4/groups'
    head = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    res = get(url=url, headers=head)
    group = res.json()
    group = group['groups'][0]['guid']
    url = 'https://api-ssl.bitly.com/v4/shorten'
    head.pop('Accept')
    head['Content-Type'] = 'application/json'
    options = {
        'long_url': links,
        'group_guid': group
    }
    res = post(url=url, headers=head, json=options)
    if res.status_code == 200:
        return res.json()['link']
    else:
        return res.json()['description']


links = 'https://www.youtube.com/watch?v=z06x6NefiDI&t=635s'
token = '25730cb4191ea00120df4bbcf6262a1b4a5a8416'
# token = '17c09e22ad155405159ca1977542fecf00231da7'
short = short_link(links=links, token=token)
print(short)
par = {
    'unit': 'day',
    'units': '-1'

}
url = f'https://api-ssl.bitly.com/v4/bitlinks/{short[7:]}/clicks/summary'
res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=par)
print(res.json())
