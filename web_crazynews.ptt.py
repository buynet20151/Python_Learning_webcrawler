import requests
import json

# 狂新聞網頁已掛
for p in range(0, 50):
    url = "https://crazy.ck101.com/category/more"
    d = {"id": "1", "page": str(p + 1)}
    print("處理頁面:", p + 1)
    response = requests.post(url, data=d)
    # 內容.text
    # urllib = json.load(response)
    # request = json.loads(response.text)
    # news List   n Dict
    news = json.loads(response.text)
    for n in news:
        url = "https://crazy.ck101.com/post/" + str(n["id"])
        print(n["crazy_rating"], n["title"], url)
