from requests import get, post, HTTPError
from urllib.parse import urlparse
import logging
import os
from dotenv import load_dotenv
import argparse


def is_bitly(link):
    """
    Проверка: является ли ссылка длинным адресом или короткой ссылкой Byt.ly
    :param link: ссылка на проверку
    :return: False - длинный адрес, True - короткая ссылка Byt.ly.
    """
    url = f'https://api-ssl.bitly.com/v4/expand'
    options = {'bitlink_id': link}
    res = post(url=url, headers=head, json=options)
    logging.info(f'is_bitly - {res.status_code}')
    return res.ok


def short_links(link):
    """
    Укорачивание длинного url в короткую ссылку Byt.ly
    :param link: длинный адрес
    :return:  строка - короткая ссылка Byt.ly
    """
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
    """
    Запрашивате общее количество кликов на данный момент
    :param link: сылка Byt.ly для проверки
    :return: число кликов
    """
    params = {
        'unit': 'day',
        'units': '-1'
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=params)
    logging.info(f'Get_total_click - {res.status_code}')
    res.raise_for_status()
    return res.json()["total_clicks"]


def click_for_day(link):
    """
    Запрашивает статистику переходов по дням, иначе HTTPError
    :param link: ссылка Byt.ly для проверки
    :return: словарь вида: {дата в формате datetime: количество кликов}
    """
    params = {
        'unit': 'day',
        'units': '-1'
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks'
    res = get(url=url, headers={'Authorization': f'Bearer {token}'}, params=params)
    logging.info(f'Click_for_day - {res.status_code}')
    res.raise_for_status()
    return res.json()['link_clicks']


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv("BYTLY_TOKEN")
    head = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    parse = argparse.ArgumentParser()
    parse.add_argument('link', help='Enter link to verify', type=str)
    parse.add_argument('-l', '--logINFO',
                       help='message level entry LOG(default: WARNING)',
                       default='WARNING',
                       choices=['CRITICAL',
                                'ERROR',
                                'WARNING',
                                'INFO',
                                'DEBUG',
                                'NOTSET'])
    argum = parse.parse_args()
    logging.basicConfig(level=argum.logINFO)
    try:
        link = argum.link
        link_new = urlparse(link)[1] + urlparse(link)[2]
        if is_bitly(link=link_new):
            print(f'Total clicks: {get_total_click(link_new)}')
            for date in click_for_day(link_new):
                y, m, d = date['date'][0:10].split('-')
                print(f'{d}/{m}/{y}  is  {date["clicks"]} clicks')
        else:
            print(short_links(link))
    except HTTPError as e:
        status, text = e.response.status_code, e.response.json()['message']
        print(f'Your link shows : {status} with message {text}')
