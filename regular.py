import json
import re
def reJson():
    ll = '{"_data":{"cid":"10000177","cname":"","eid":"600170392","first_login":"0","uid":"602789520","userkey":"1542091777-ced2cd8129068af480361fef2ef31df8","phone":"13012345678","_ret":"0","_errCode":"0","_errStr":"OK"}}'
    b = "userkey"
    regex = '\"' + b + '\":\".+?\"'
    print(regex)
    ls = re.findall(regex, ll)
    print(ls)
    jsonStr = '{%s}' % ls[0]
    js = json.loads(jsonStr)
    print(js)
    print(type(js))

if __name__ == '__main__':
    reJson()