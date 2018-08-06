import requests
import re


# http://www.dyhjw.com/hjtd/

'''
<span class="nom last red|green">275.63</span>

<span class="unit">（元/克）</span>

<span class="bfb"><font class="swing">+1.02</font><font class="swingRange">+0.37%</font>
</span>
'''


def get_gold_price():
    gold_url = 'http://www.dyhjw.com/hjtd/'
    req = requests.get(gold_url, ).content.decode(encoding='utf-8')
    # print(req)

    key = []
    reg = ['<span class="nom last .*?">(.*?)</span>',
           '<font class="swing">(.*?)</font>',
           '<font class="swingRange">(.*?)</font>']

    for i in reg:
        key.append(re.search(i, req, re.S).group(1))

    return key


def send_to_ftqq():
    p = get_gold_price()

    msg = '- 实时价格: **{0}**元/克\n\n' \
          '- 价格浮动: **{1}**元/克 ({2})\n\n' \
          '- ref：[dyhjw.com/hjtd/](http://www.dyhjw.com/hjtd/)'
    msg = msg.format(p[0], p[1], p[2])

    key = 'SCU10033T765c015c42529885b78aeb3545725a9d5ac305375cc59'
    api = 'https://sc.ftqq.com/{}.send?text={}&desp={}'

    api = api.format(key, 'Gold_Price', msg)
    requests.post(api)


# send_to_ftqq()
