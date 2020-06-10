import requests
import json
from requests import exceptions, Request, Session
from contextlib import closing

URL = 'http://sale-web.live-test.lemobar.cn'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_output(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    response = requests.get(build_uri('web/v1/index'))
    print(better_output(response.text))


def params_method():
    try:
        response = requests.get(build_uri('web/v1/role-brand'), params={'page': 1, 'rows': -1}, timeout=0.01)
    except exceptions.Timeout as e:
        print(str(e))
    else:
        print(better_output(response.text))
        print(response.headers)
        print(response.url)
        print(response.status_code)


def json_method():
    response = requests.post(build_uri('web/v1/role-brand'), json={'page': 1, 'rows': -1})
    print(better_output(response.text))
    print(response.headers)
    print(response.url)
    print(response.status_code)


def custom_method():
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    request = Request('Get', build_uri('web/v1/role-brand'), auth=('xxxx', 'xxxx'), headers=headers)
    prepped = request.prepare()
    print(prepped.body)
    print(prepped.headers)

    response = s.send(prepped, timeout=5)
    print(response.status_code)
    print(response.headers)
    print(response.text)


def download_image():
    url = 'http://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=selenium' \
          '&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined' \
          '&cs=1692111363,2308363575&os=3986993180,1297226092&simid=3380610483,312453899&pn=0&rn=1&di=92290' \
          '&ln=1826&fr=&fmq=1591261659117_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=' \
          'undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=http%3A%2F%2Ffile.' \
          'do.yy.com%2Fgroup3%2FM04%2FCB%2F14%2Ftz0MYFZWeoiAMEsTAAArFEdujpc127.jpg&rpstart=0&rpnum=0&adpicid=0' \
          '&force=undefined'
    response = requests.get(url)
    print(response.status_code)
    print(response.content)


def download_image2():
    url = 'http://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=selenium' \
          '&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined' \
          '&cs=1692111363,2308363575&os=3986993180,1297226092&simid=3380610483,312453899&pn=0&rn=1&di=92290' \
          '&ln=1826&fr=&fmq=1591261659117_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined' \
          '&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=http%3A%2F%2' \
          'Ffile.do.yy.com%2Fgroup3%2FM04%2FCB%2F14%2Ftz0MYFZWeoiAMEsTAAArFEdujpc127.jpg&rpstart=0&rpnum=0' \
          '&adpicid=0&force=undefined'
    # response = requests.get(url, stream=True)
    with closing(requests.get(url, stream=True)) as response:
        with open('venv/selenium.png', 'wb') as file:
            for data in response.iter_content(128):
                file.write(data)
    print(response.status_code)


def basic_auth():
    response = requests.get(build_uri('web/v1/role-brand'), auth=('xxxxx', 'xxxxxx'))
    print(response.status_code)
    print(response.text)
    print(response.request.headers)


# basic_auth()


if __name__ == '__main__':
    basic_auth()
