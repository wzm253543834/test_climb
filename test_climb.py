import pandas
import requests
from lxml import etree
from bs4 import BeautifulSoup


url = "https://book.douban.com/subject/26829016/comments/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                       " Chrome/79.0.3945.130 Safari/537.36"}
r = requests.get(url, headers=header).text
x = etree.HTML(r)
ret = x.xpath('//*[@id="comments"]')
print(ret)
soup = BeautifulSoup(r, 'lxml')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    print(item.string)
comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv('data.csv')
