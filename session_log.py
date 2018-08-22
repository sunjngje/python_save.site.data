import pq
import requests
import re
import pymysql.cursors

def inster(datak):
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',
        port=xxx,
        user='xxx',
        passwd='xxx',
        db='xxx',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()
    # 插入数据
    sql = "INSERT INTO kkk (num, name, kind, kindone, tel, kindtwo, time, os, status) VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',  )"
    data = (datak['num'], datak['name'], datak['kind'], datak['kindone'], datak['tel'], datak['kindtwo'], datak['time'], datak['os'], datak['status'])
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')

def getContent(url):
    # 使用requests.get获取知乎首页的内容
    r = requests.get(url)
    # request.get().content是爬到的网页的全部内容
    return r.content


# 获取_xsrf标签的值
def getXSRF(url):
    # 获取知乎首页的内容
    content = getContent(url)
    # 正则表达式的匹配模式
    pattern = re.compile('.*?<input type="hidden" name="_xsrf" value="(.*?)"/>.*?')
    # re.findall查找所有匹配的字符串
    match = re.findall(pattern, content)
    xsrf = match[0]
    # 返回_xsrf的值
    return xsrf


# 登录的主方法
def login():
    # 获取验证码
    codeurl = 'xxxxxxxx'
    valcode = requests.get(codeurl)
    f = open('valcode.png', 'wb')
    # 将response的二进制内容写入到文件中
    f.write(valcode.content)
    # 关闭文件流对象
    f.close()
    code = input('请输入验证码：')
    u = input('请输入u：')
    p = input('请输入p：')
    # post需要的表单数据，类型为字典
    login_data = {
        'password': p,
        "code": str(code),
        'username': u,
    }

    # 设置头信息
    headers_base = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'xxxxxxxxx',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        'Referer': 'http://xxxxxx/',
    }
    # 使用seesion登录，这样的好处是可以在接下来的访问中可以保留登录信息
    session = requests.session()
    # 登录的URL
    baseurl = "xxxxxxxxxx"
    # requests 的session登录，以post方式，参数分别为url、headers、data
    content = session.post(baseurl, headers=headers_base, cookies=requests.utils.dict_from_cookiejar(valcode.cookies),data=login_data)
    # 成功登录后输出为 {"r":0,"msg": "\u767b\u9646\u6210\u529f"}
    print(content.text)
    array = {
        'headers': headers_base,
        'cookies': requests.utils.dict_from_cookiejar(valcode.cookies),
        'data': login_data
    }
    return array
    # 再次使用session以get去访问知乎首页，一定要设置verify = False，否则会访问失败


# url = "http://kak168.com"
# 进行登录，将星号替换成你的知乎登录邮箱和密码即可

# strpattern = r'(?<=<table class="tCenter tab w100 f14 ml15" cellspacing="0">).+?(?=</table>)'
# pt = re.compile(strpattern, re.S)
# mch1 = re.search(pt, line)
# dom = pq(mch1.group(0))('td')
# # dom = pq(mch1.group(0))('tr') #获取这个table中所有标签tr
# for it in dom.items(): #遍历每一个tr
#     print(it) #输出每个tr的内容
# m = re.findall(r'<table class="tCenter tab w100 f14 ml15" cellspacing="0">(.*)</table>', line, re.I|re.M)
# print(line)
def cont(headers=None, cookies=None, data=None,):
    session = requests.session()
    for i in range(1, 301):
        s = session.get("xxxxxxxxx" + str(i), headers=headers, cookies=cookies, data=data)
        # 把爬下来的知乎首页写到文本中
        # f = open('test3.txt', 'w')
        # f.write(s.text.encode('utf-8'))
        #     print(s.text)
        #     return s.text
        #     '<td[^>]*>[^<]*</td>' <td( .*?)?>.*?</td> <td>(.*)</td>
        fp = open('new_k2.txt', 'a')
        fp.write(str(i)+'页')
        fp.write("\n")
        fp.close()
        print(str(i)+'页')
        m = re.findall('<td>([^<]*.*?)</td>', s.text, re.I | re.M)
        # print(m);break
        #sum(m)
        #print(str(m).count("1"));
        # if m:
        #     for x in m:
        #         fp = open('new_k11.txt', 'a')
        #         try:
        #             fp.write(x.strip())
        #         except Exception as e:
        #             fp.write('信息为空或有误')
        #         if x > 0:
        #             fp.write('-------')
        #         # check_w = fp.write(x.strip())
        #         # if not check_w:
        #         #     fp.write('信息为空或有误')
        #         fp.write("\n")
        #         fp.close()
        #         print(x.strip())
        # print(m.split())
        ii = 0
        if m:
            for x in m:
                fp = open('new_k2.txt', 'a')
                try:
                    fp.write(x.strip())
                    fp.write("\n")
                except Exception as e:
                    fp.write('信息为空或有误')
                    fp.write("\n")
                ii = ii + 1
                if ii%10 == 0 or ii%10 == 10 or ii/10 == 10:
                    fp.write("----")
                    fp.write("\n")
            print(ii)
            fp.write("\n")







def main():
    line = login()
    print(line)
    cont(line['headers'], line['cookies'], line['data'])


main()
