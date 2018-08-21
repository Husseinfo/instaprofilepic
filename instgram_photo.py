#!/usr/bin/env python3

from json import loads
from re import compile

from bs4 import BeautifulSoup
from requests import get


def get_profile_pic(user):
    try:
        user = user.replace('@', '')
        url = f'https://instagram.com/{user}'
        soup = BeautifulSoup(get(url).content, 'html.parser')
        script = soup.find('script', text=compile('window\._sharedData')).text
        script = script.split('window._sharedData = ')[1].split(';')[0]
        data = loads(script)
        user_id = data['entry_data']['ProfilePage'][0]['graphql']['user']['id']
        info_url = f'https://i.instagram.com/api/v1/users/{user_id}/info/'
        json = loads(get(info_url).content)
        link = json['user']['hd_profile_pic_url_info']['url']
        return link
    except Exception as e:
        print(e)
        return None
