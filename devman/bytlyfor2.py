from requests import get, post, HTTPError
from urllib.parse import urlparse
import logging


def is_bitly(link):
    url = f'https://api-ssl.bitly.com/v4/expand'
    options = {'bitlink_id': link}
    res = post(url=url, headers=head, json=options)
    logging.info(f'is_bitly - {res.status_code}')
    return res.ok


def short_links(link):
    url = 'https://api-ssl.bitly.com/v4/groups'
    res = get(url=url, headers=head)
    group = res.json()['groups'][0]['guid']
    url = 'https://api-ssl.bitly.com/v4/shorten'
    head.pop('Accept')
    head['Content-Type'] = 'application/json'
    options = {
        'group_guid': group,
        'long_url': link
    }
    res = post(url=url, headers=head, json=options)
    logging.info(f'Short_links - {res.status_code}')
    res.raise_for_status()
    return res.json()['link']


def get_total_click(link):
    params = {
        'unit': 'day',
        'units': '-1'
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=params)
    logging.info(f'Get_total_click - {res.status_code}')
    res.raise_for_status()
    return res.json()["total_clicks"]

# f'Ваша ссылка вернула код: {res.status_code} с сообщением {res.json()["message"]}'


def click_for_day(link):
    params = {
        'unit': 'day',
        'units': '-1'
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks'
    res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=params)
    logging.info(f'Click_for_day - {res.status_code}')
    res.raise_for_status()
    return res.json()['link_clicks']


#link = 'https://bit.ly/2HwXQF9'
# link = 'http://bit.ly/2OaMRRO'
# link = 'http://ifserial.club/serials/drama/khoroshij_doktor_90/6-1-0-283'
link = 'http://bit.ly/2JUrR1I'
token = '25730cb4191ea00120df4bbcf6262a1b4a5a8416'

head = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json'
}

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    try:
        print(link)
        bitlink = urlparse(link)[1] + urlparse(link)[2]
        if is_bitly(link=bitlink):
            print(f'Общее количество кликов: {get_total_click(bitlink)}')
            for date in click_for_day(bitlink):
                y, m, d = date['date'][0:10].split('-')
                print(f'{d}/{m}/{y} года по ней было {date["clicks"]} переходов')
        else:
            short = short_links(link)
            print(short)
    except HTTPError as e:
        status, text = e.response.status_code, e.response.json()['message']
        print(f'Ваша ссылка вернула код: {status} с сообщением {text}')

