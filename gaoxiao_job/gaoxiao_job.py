# coding=UTF-8
import requests
from bs4 import BeautifulSoup


def get_job_list():
    # 南京高校人才网
    gao_xiao_url = 'http://www.gaoxiaojob.com/zhaopin/gaoxiao/nanjing/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/57.0.2987.133'}

    res = requests.get(gao_xiao_url, headers=headers)
    # soup = BeautifulSoup(res.content, 'lxml')
    soup = BeautifulSoup(res.content, 'html.parser')
    # print(soup.title.string)

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

    job_list = '[gaoxiaojob.com](http://www.gaoxiaojob.com/zhaopin/gaoxiao/nanjing/)\n\n'
    for div in job_div:
        # 获得日期、网址、描述、人数、截止日期

        date = div.span.small.get_text()
        web = div.span.a.get('href')
        des = div.span.a.get_text()


        job = '1. [{} {}]({})\n\n'.format(date, des, web)
        job_list += job


    return job_list


def send_to_ftqq():
    msg = get_job_list()

    with open('ftqq.ini', 'rb') as f:
        key = f.readline().decode('utf8')
        api = 'https://sc.ftqq.com/{}.send?text={}&desp={}'

        api = api.format(key, 'Nanjing_Jobs', msg)
        requests.post(api)


# send_to_ftqq()
