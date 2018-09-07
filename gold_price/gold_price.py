# coding=UTF-8

import requests
import json
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/57.0.2987.133'}


def get_gold_price():

    gold_url = 'http://www.dyhjw.com/hjtd/'

    req = requests.get(gold_url, ).content.decode(encoding='utf-8')
    res = requests.get(gold_url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')

    '''
    <span class="nom last red|green">275.63</span>

    <span class="unit">（元/克）</span>

    <span class="bfb"><font class="swing">+1.02</font><font class="swingRange">+0.37%</font>
    </span>
    '''
    price = soup.find('span', {'class': ['nom last red', 'nom last green']}).text
    swing = soup.find('font', {'class': 'swing'}).text
    range = soup.find('font', {'class': 'swingRange'}).text

    print(price, swing, range)

    return [price, swing, range]


def send_to_ftqq(text, desp):
    with open('../config.json', encoding='utf-8') as f:
        config = json.load(f)
        key = config['ftqq']
        print(key)

        api = 'https://sc.ftqq.com/{}.send'.format(key)
        send_data = {'text': text, 'desp': desp}
        res = requests.post(api, headers=headers, data=send_data)
        print(res.content)


title = 'Gold_Price'
gp = get_gold_price()
content = '实时价格:{0}元/克\n上浮/下降:{1}元/克({2})\n'.format(gp[0], gp[1], gp[2])
send_to_ftqq(title, content)