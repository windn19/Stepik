from requests import post, get


def short_link(links, token):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    head = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    options = {
        'long_url': links,
        'group_guid': 'Bj4uewAKgEY'
    }
    res = post(url=url, headers=head, json=options)
    if res.status_code == 200:
        return res.json()['link']
    else:
        return res.json()['description']


def click(links, token):
    par = {
        'unit': 'day',
        'units': '-1'
    }

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{links[7:]}/clicks/summary'
    res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=par)
    if res.status_code == 200:
        print(f'Общее количество кликов по ссылке: {res.json()["total_clicks"]}')
        url = f'https://api-ssl.bitly.com/v4/bitlinks/{links[7:]}/clicks'
        res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=par)
        data = res.json()
        for day in data['link_clicks']:
            print(f'{day["date"]} было {day["clicks"]} переход')
        return True
    return False


links = 'https://www.youtube.com/watch?v=z06x6NefiDI&t=635s'
token = '25730cb4191ea00120df4bbcf6262a1b4a5a8416'
links = input('ВВедите ссылку: ')
if not click(links=links, token=token):
    print(short_link(links=links, token=token))
# http://bit.ly/2vV9FOC
# Bj4uewAKgEY