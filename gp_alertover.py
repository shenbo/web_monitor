import requests
from gold_price_monitor.gold_price import get_gold_price


def gp_alertover():
    # alertover api
    ao_api = 'https://api.alertover.com/v1/alert'
    ao_source = 's-1aff8663-daa0-45c6-9a0c-92979f32'
    ao_receiver = 'g-3a878513-8ca3-4e72-b3bb-c467a5da'

    # msg
    pr = get_gold_price()
    msg = '实时价格:  {0} 元/克 \n' + '上浮/下降: {1} 元/克 ({2}) \n'
    msg_title = 'Gold Price'
    msg_content = msg.format(pr[0], pr[1], pr[2])

    post_data= {'source': ao_source,
                'receiver': ao_receiver,
                'content': msg_content,
                'title': msg_title
                }

    res = requests.post(ao_api, data=post_data)

    print(res.text)

# gp_alertover()
