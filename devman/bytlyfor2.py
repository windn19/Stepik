from requests import get, post


def is_bitly(links):
    url = f'https://api-ssl.bitly.com/v4/expand'

    head = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }

    opt = {'bitlink_id': links[-14:]}
    res = post(url=url, headers=head, json=opt)
    return res.ok


def short_links(links):
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
    return f'Ваша ссылка вернула код: {res.status_code} с сообщением {res.json()["message"]}'


def get_total_click(links):
    par = {
        'unit': 'day',
        'units': '-1'
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{links[7:]}/clicks/summary'
    res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=par)
    if res.status_code == 200:
        return (f'Общее количество кликов: {res.json()["total_clicks"]}')
    return f'Ваша ссылка вернула код: {res.status_code} с сообщением {res.json()["message"]}'


def click_for_day(links):
    par = {
        'unit': 'day',
        'units': '-1'
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{links[7:]}/clicks'
    res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=par)
    if res.status_code == 200:
        for date in res.json()['link_clicks']:
            y, m, d = date['date'][0:10].split('-')
            print(f'{d}/{m}/{y} года по ней было {date["clicks"]} переходов')


# links = 'https://bit.ly/2HwXQF9'
#links = 'http://bit.ly/2OaMRRO'
links = 'http://lfserial.club/serials/drama/khoroshij_doktor_90/6-1-0-283'
token = '25730cb4191ea00120df4bbcf6262a1b4a5a8416'
if __name__ == '__main__':
    print(links)
    if is_bitly(links=links):
        print(get_total_click(links))
        click_for_day(links)
    else:
        short = short_links(links)
        print(short)
