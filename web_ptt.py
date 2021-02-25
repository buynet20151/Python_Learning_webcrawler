# from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from jieba.analyse import extract_tags
import requests

url = "https://www.ptt.cc/bbs/Gossiping/M.1601995372.A.ABD.html"
# r = Request(url)
# r .add_header("user-agent", "Mozilla/5.0")
# response = urlopen(r)
response = requests.get(url, cookies={"over18": "1"})
html = BeautifulSoup(response.text)

content = html.find("div", id="main-content")

metas = content.find_all("span", class_="article-meta-value")
print("ID:", metas[0].text)
print("看板:", metas[1].text)
print("標題:", metas[2].text)
print("時間:", metas[3].text)

# extract 人間蒸發
ms = content.find_all("div", class_="article-metaline")
for m in ms:
    m.extract()
ms = content.find_all("div", class_="article-metaline-right")
for m in ms:
    m.extract()
pushes = content.find_all("div", class_="push")
score = 0
for p in pushes:
    tag = p.find("span", class_="push-tag").text
    if "推" in tag:
        score += 1
    elif "噓" in tag:
        score -= 1
    p.extract()
print("分數:", score)
print("本文:", content.text)
print("關鍵字:", extract_tags(content.text), 10)
