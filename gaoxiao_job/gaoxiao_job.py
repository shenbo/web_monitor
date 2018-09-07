# coding=UTF-8

import requests
import json
from bs4 import BeautifulSoup


# 南京高校人才网
gao_xiao_url = 'http://www.gaoxiaojob.com/zhaopin/gaoxiao/nanjing/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/57.0.2987.133'}


def get_job_list():
    res = requests.get(gao_xiao_url, headers=headers)
    # soup = BeautifulSoup(res.content, 'lxml')
    soup = BeautifulSoup(res.content, 'html.parser')
    print(soup.title.string)

    # 网页中关于描述的div格式
    '''
    <div class="style2 stylebg"> 
        <span class="ltitle">
            <small>(08.02)</small>
            <a href="http://www.gaoxiaojob.com/zhaopin/gaoxiaojiaoshi/20180802/319536.html">
                .南京大学物理学院关于2018年8月公开招聘1名专职科研人员的启事
            </a>
        </span> 
        <span class="ltime">2018年8月15日</span> 
        <span class="lcompany">
            <a href="http://www.gaoxiaojob.com/zhaopin/chengshi/nanjing/" target="_blank">南京</a> 
        </span>  
        <span class="lsalary">1名</span> 
    </div>
    '''

    # 获得列表
    job_div = soup.find_all('div', {'class': 'style2'})
    # print(job_div)
    job_list = '[gaoxiaojob.com]({})\n\n---\n\n'.format(gao_xiao_url)
    for div in job_div:
        # 获得日期、网址、描述、人数、截止日期

        date = div.span.small.get_text()
        web = div.span.a.get('href')
        des = div.span.a.get_text()

        job = '1. [{} {}]({})\n\n'.format(date, des, web) # markdown格式
        job_list += job

    return job_list


def send_to_ftqq(text, desp):
    with open('../config.json', encoding='utf-8') as f:
        config = json.load(f)
        key = config['ftqq']
        print(key)

        api = 'https://sc.ftqq.com/{}.send'.format(key)
        send_data = {'text': text, 'desp': desp}
        res = requests.post(api, headers=headers, data=send_data)
        print(res.content)


title = '南京高校招聘'
content = get_job_list()
send_to_ftqq(title, content)
