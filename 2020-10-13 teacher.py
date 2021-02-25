import requests

# x=["a","b","c","d","e","f","g","1","2","3","4","5","6","7","8","9","0"]
# def pwdList(i,p):
# 	global x
# 	ret=[]
# 	for d in x:
# 		ret+=[p+d]
# 		if i>1:
# 			ret+=pwdList(i-1,p+d)
# 	return ret

# for pwd in pwdList(2,""):
# 	r=requests.post(
# 		"http://teaching.bo-yuan.net/",
# 		params={
# 			"uid":"5f8502f002a34"
# 		},
# 		data={
# 			"ex[class]":"5f7b087a7815a",
# 			"ex[username]":"99測試",
# 			"ex[password]":pwd
# 		},
# 		headers={
# 			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
# 			"Cookie":"PHPSESSID=e7f25u9pe7iok0mq57dnd09j37"
# 		}
# 	)
# 	r.encoding="utf8"

# 	r=requests.get(
# 		"http://teaching.bo-yuan.net/",
# 		headers={
# 			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
# 			"Cookie":"PHPSESSID=e7f25u9pe7iok0mq57dnd09j37"
# 		}
# 	)
# 	r.encoding="utf8"
# 	if "個人資料管理" in r.text:
# 		print("登入成功，密碼是：",pwd)
# 		break
# 	else:
# 		print("登入失敗，密碼不是：",pwd)


import csv
import codecs
import io
# with codecs.open("1.csv","r","utf8") as f:
# 	data=list(csv.reader(f))
# 	print(data)

# r=requests.get(
# 	"https://data.taipei/api/getDatasetInfo/downloadResource",
# 	params={
# 		"id":"b1398491-07fe-40da-bb5a-ae73f4e45984",
# 		"rid":"9099acc7-9b9e-4a99-8c0f-3c85cd578a97"
# 	},
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
# 	}
# )
# r.encoding="big5"
# data=list(csv.reader(io.StringIO(r.text)))
# for d in data:
# 	print(d)

import json
# r=requests.get(
# 	"https://data.taipei/api/v1/dataset/9099acc7-9b9e-4a99-8c0f-3c85cd578a97",
# 	params={
# 		"scope":"resourceAquire"
# 	},
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
# 	}
# )
# print(json.loads(r.text))
# data=json.loads(r.text)
# for d in data["result"]["results"]:
# 	print(d["Bus"],d["Destination"])
# for p in range(1,6):
# 	r=requests.get(
# 		"https://udn.com/api/more",
# 		params={
# 			"page":p,
# 			"id":"",
# 			"channelId":"1",
# 			"cate_id":"0",
# 			"type":"breaknews",
# 			"totalRecNo":"9759"
# 		},
# 		headers={
# 			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
# 		}
# 	)
# 	data=json.loads(r.text)
# 	for d in data["lists"]:
# 		print(d["title"])

from bs4 import BeautifulSoup

# r=requests.get(
# 	"https://money.udn.com/rank/newest/1001/0/1",
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
# 	}
# )
# print(r.text)

# b=BeautifulSoup(r.text, "html.parser")
# for d in b.find_all("tr"):
# 	if d.find("td")!=None:
		# p=d.find_all("td")
		# print(p[1].text,p[0].text)

# b=BeautifulSoup(r.text, "html.parser")
# fn=0
# img=0
# for d in b.find_all("tr"):
# 	if d.find("td")!=None:
# 		category=d.find("td",{"class":"only_web"}).text
# 		title=d.find("td").text
# 		url=d.find("td").find("a").attrs["href"]
# 		r2=requests.get(
# 			url,
# 			headers={
# 				"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
# 			}
# 		)
# 		b2=BeautifulSoup(r2.text, "html.parser")
# 		content=b2.find("div",{"id":"article_body"}).text
# 		fn+=1
# 		with codecs.open("news/"+str(fn)+".txt","w","utf8") as f:
# 			f.write(url+"\r\n")
# 			f.write(category+"\r\n")
# 			f.write(title+"\r\n\r\n")
# 			f.write(content+"\r\n")
# 		for m in b2.find("div",{"id":"article_body"}).find_all("img"):
# 			r3=requests.get(
# 				m.attrs["src"],
# 				headers={
# 					"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
# 				}
# 			)
# 			img+=1
# 			with codecs.open("images/"+str(img)+".jpg","wb") as f:
# 				f.write(r3.content)


r1=requests.get(
	"https://www.taiwan.net.tw/m1.aspx",
	params={
		"sNo":"0001001"
	},
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
	}
)
b1=BeautifulSoup(r1.text, "html.parser")
fn=0
for d1 in b1.find_all("div",{"class":"columnBlock"}):
	date=d1.find("span",{"class":"date"}).text
	title=d1.find("a",{"class":"columnBlock-title"}).text
	imgurl=d1.find("img").attrs["data-src"]
	url="https://www.taiwan.net.tw/"+d1.find("a",{"class":"columnBlock-title"}).attrs["href"]
	r3=requests.get(
		url,
		headers={
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
		}
	)
	b2=BeautifulSoup(r3.text, "html.parser")
	content=""
	for d2 in b2.find("div",{"class":"content"}).find_all("p"):
		content+=d2.text+"\r\n"
	fn+=1
	with codecs.open("news2/"+str(fn)+".txt","w","utf8") as f:
		f.write(date+"\r\n")
		f.write(title+"\r\n\r\n")
		f.write(content+"\r\n")
	r2=requests.get(
		imgurl,
		headers={
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
		}
	)
	with codecs.open("news2/"+str(fn)+".jpg","wb") as f:
		f.write(r2.content)