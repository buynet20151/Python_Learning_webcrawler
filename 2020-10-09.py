# import colorama

# colorama.init(True)

# print("ABC")
# print(colorama.Style.BRIGHT+"ABC")
# print(colorama.Fore.RED+"ABC")
# print(colorama.Back.GREEN+"ABC")

import requests
import codecs


# r = requests.get(
# 	"https://www.taiwan.net.tw/m1.aspx?sNo=0001001"
# )
# print(r.status_code
# print(r.headers)
# for k,v in r.headers.items():
# 	print(k, ":",v)
# print(r.encoding)
# r.encoding="big5"
# with codecs.open("1.html","w","utf8") as f:
# 	f.write(r.text)


# with codecs.open("1.jpg","wb") as f:
# 	f.write(r.content)
# for p in range(1,6):
# 	r = requests.get(
# 		"https://www.taiwan.net.tw/m1.aspx",
# 		params={
# 			"sNo":"0001001",
# 			"page":p
# 		}
# 	)
# 	with codecs.open("html/"+str(p)+".html","w","utf8") as f:
# 		f.write(r.text)

# r = requests.post("https://www.ntub.edu.tw/app/index.php",
# 	params={
# 		"Action":"mobileloadmod",
# 		"Type":"mobile_asso_cg_mstr",
# 		"Nbr":"1003"
# 	}
# )
# print(r.text)
# with codecs.open("html/2.html","w","utf8") as f:
# 		f.write(r.text)


# r = requests.post(
# 	"http://teaching.bo-yuan.net/",
# 	params={
# 		"uid":"5f8016b2df655"
# 	},
# 	data={
# 		"ex[class]":"5f7b087a7815a",
# 		"ex[username]":"28林豈禾",
# 		"ex[password]":"a93afa"
# 	},
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
# 		"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
# 	}
# )

r = requests.post(
	"http://teaching.bo-yuan.net/",
	
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
		"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	}
)
r.encoding="utf8"
with codecs.open("23.html","w","utf8") as f:
	f.write(r.text)

