from requests import post, get


def short_link(links):
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
        'group_guid': group,
        'long_url': links
    }
    res = post(url=url, headers=head, json=options)
    if res.status_code == 200 or res.status_code == 201:
        return res.json()['link']
    elif res.status_code == 400 and res.json()['message'] == 'ALREADY_A_BITLY_LINK':
        return report(links=links, token=token)
    else:
        return None


def report(links):
    par = {
        'unit': 'day',
        'units': '-1'
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{links[7:]}/clicks/summary'
    res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=par)
    if res.status_code == 200:
        print(f'Общее количество кликов: {res.json()["total_clicks"]}')
        url = f'https://api-ssl.bitly.com/v4/bitlinks/{links[7:]}/clicks'
        res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=par)
        for date in res.json()['link_clicks']:
            y, m, d = date['date'][0:10].split('-')
            return f'{d}/{m}/{y} года по ней было {date["clicks"]} переходов'
    else:
        return f'Ваша ссылка вернула код: {res.status_code} с сообщением {res.json()["message"]}'


# links = 'http://bit.ly/2HwXQF9'
# links = 'http://bit/2OaMRRO'
links = 'http://lfserial.club/serials/drama/khoroshij_doktor_90/6-1-0-283'
token = '25730cb4191ea00120df4bbcf6262a1b4a5a8416'
# token = '17c09e22ad155405159ca1977542fecf00231da7'
if __name__ == '__main__':
    print(links)
    short = short_link(links=links)
    print('Введена некорректная ссылка.' if short is None else short)
