from htmlreport import *
import os,time
import re
import requests
import json
loginUrl = 'https://mall.huishoubao.com/user/login'

if __name__ == '__main__':
    r = Result()

    # r.error_count = 1
    # r.success_count = 1
    # r.failure_count = 1
    # r.startTime = 2
    # r.stopTime = 1
    #
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # path = os.getcwd()
    # report_path = path + "\\" + "report" + "\\" + "可乐优品接口自动化测试报告" + now + ".html"
    # print(report_path)
    # fp = open(report_path, "wb")
    # rp = Report(stream=fp,title=u'可乐优品接口自动化测试',description=u'用例执行情况')
    # rp.generateReport(r)
    headers = {}
    headers['accept'] = 'application/json, text/plain, */*'
    headers['content-type'] = 'application/json;charset=UTF-8'
    headers['origin'] = 'https://mall.huishoubao.com'
    headers['content-length'] = '39'
    headers['accept-language'] = 'zh-cn'
    headers['user-agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 ' \
                            '(KHTML, like Gecko) Mobile/15G77'
    headers['referer'] = 'https://mall.huishoubao.com/index.html'
    headers['accept-encoding'] = 'br, gzip, deflate'

    j = {"phone": '13012345678', "code": '66666'}
    response = requests.post(url=loginUrl, headers=headers, json=j, verify=True)
    print(response.text)
    a = "userkey"
    regex = '\"' + a   + '\":\".+?\"'
    print(regex)
    ls = re.search(regex,response.text)
    print(ls)
    ls2 = re.findall(regex,response.text)
    print(ls2)
    jsonStr = '{%s}' % ls2[0]
    js = json.loads(jsonStr)
    print(type(js))
    str = js["userkey"]
    print(str)