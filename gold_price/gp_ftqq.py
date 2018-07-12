import requests
import gold_price


def send_to_ftqq(t, d):
    sckey = 'SCU10033T5f9a872874ef8f9babb7f5db7f198c855964a3909aa42'
    api = 'https://sc.ftqq.com/{}.send?text={}&desp={}'.format(sckey, t, d)

    requests.post(api)


if __name__ == '__main__':
    p = gold_price.get_gold_price()
    # print(p)

    msg = '实时价格:{0}元/克\n上浮/下降:{1}元/克({2})\n'
    msg = msg.format(p[0], p[1], p[2])
    send_to_ftqq('Gold Price', msg)