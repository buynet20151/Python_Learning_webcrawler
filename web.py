from urllib.request import urlopen
import json

# MAC電腦才要加的兩行
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.google.com/doodles/json/2020/9?hl=zh_TW"
response = urlopen(url)

doodles = json.load(response)
# doodles -> List d -> Dictionary
for d in doodles:
    url = "https:" + d["url"]
    print(d["title"], url)

    # 針對圖片做處理
    response = urlopen(url)
    img = (response.read())
    fname = "doodles/" + url.split("/")[-1]

    # 存檔三部曲
    f = open(fname, "wb")
    f.write(img)
    f.close()