import requests
from bs4 import BeautifulSoup


def get_job_list():
    # 南京高校人才网
    gao_xiao_url = 'http://www.gaoxiaojob.com/zhaopin/gaoxiao/nanjing/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/57.0.2987.133'}

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

    job_list = ''
    html_list = ''
    for div in job_div:
        # 获得日期、网址、描述、人数、截止日期

        date = div.span.small.get_text()
        web = div.span.a.get('href')
        des = div.span.a.get_text()
        # job = date + web + des
        # print(job)
        #
        # job_list += job + '\n'

        html = '<a href=\"{}\"> {} {} </a> <br><br>'.format(web, date, des)
        html_list += html + '\n'


    return html_list


from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


def send_mail(mail_title='', mail_content=''):
    sender_qq_mail = '405122738@qq.com'
    receiver = 'shenbo@hotmail.com'

    # pwd为qq邮箱的授权码
    pwd = 'ucalyvqvxszxcafc'
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'

    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel: 参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq_mail, pwd)

    msg = MIMEText(mail_content, "html", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()


mail_title = '南京高校招聘'
mail_content = get_job_list()

send_mail(mail_title=mail_title, mail_content=mail_content)

