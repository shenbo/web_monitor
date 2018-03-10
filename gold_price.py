import requests
import re


# url = 'http://www.dyhjw.com/hjtd/'

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

    # print(key)

    # reg2 = '<font>(.*?)</font></li>'
    # key2 = (re.findall(reg1, req, re.S))
    #
    # print(key2)

    return key

# get_gold_price()
