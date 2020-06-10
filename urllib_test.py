import urllib.request
r = urllib.request.urlopen('http://www.baidu.com', data=None, timeout=10)
print(r.info())
