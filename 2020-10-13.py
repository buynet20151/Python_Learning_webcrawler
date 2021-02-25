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

# print(pwdList(2,""))



# def pwdList(i,p):
# 	global x
	
# 	for d in x:
		
# 		if i>1:
# 			ret=pwdList(i-1,p+d)
# 			print(ret)
# pwdList(2,"")


# for pwd in range(0, 100):
# 	r = requests.post(
# 		"http://teaching.bo-yuan.net/",
# 		params={
# 			"uid":"5f85034727cf3"
# 		},
# 		data={
# 			"ex[class]":"5f7b087a7815a",
# 			"ex[username]":"98實驗",
# 			"ex[password]":pwd
# 		},
# 		headers={
# 			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
# 			"Cookie":"PHPSESSID=2b72ino2ok1mgvpuntj4r0o594"
# 		}
# 	)
# 	r.encoding="utf8"

# 	r = requests.post(
# 		"http://teaching.bo-yuan.net/",
# 		headers={
# 			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
# 			"Cookie":"PHPSESSID=2b72ino2ok1mgvpuntj4r0o594"
# 		}
# 	)
# 	r.encoding="utf8"
# 	if "個人資料管理" in r.text:
# 		print("登入成功, 密碼是:",pwd)
# 		break
# 	else:
# 		print("登入失敗!, 密碼是:",pwd)


import csv
import codecs
import io
import json
# with codecs.open("1.csv","r","utf8") as f:
# 	data=list(csv.reader(f))
#  	print(data)

# r = requests.get(
# 	"https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download",
# 	params={
# 		"id":"6004552b-5679-4c07-8bfe-68a3783853db",
# 		"rid":"bf59d514-2015-4113-a88f-bad3be1a7062"
# 	},
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

# 	}
# )
# r.encoding="utf8"
# print(r.text)
# data=list(csv.reader(io.StringIO(r.text)))
# for d in data:
# 	print(d)

# r = requests.get(
# 	"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0002-001?",
# 	params={
# 		"Authorization":"rdec-key-123-45678-011121314",
# 		"format":"JSON"
# 	},
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
# 	}
# )
# data=json.loads(r.text)
# print(data)

# from bs4 import BeautifulSoup
# r = requests.get(
# 	"https://money.udn.com/rank/newest/1001/0/1",
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

# 	}
# )
# 抓出標題
# b=BeautifulSoup(r.text,"html.parser")
# for d in b.find_all("tr"):
# 	if d.find("td")!=None:
# 		print(d.find("td").text)

# 取索引
# b=BeautifulSoup(r.text,"html.parser")
# for d in b.find_all("tr"):
# 	if d.find("td")!=None:
# 		p=d.find_all("td")	
# 		print(p[1].text,p[0].text)

# 用類別抓出
# b=BeautifulSoup(r.text,"html.parser")
# for d in b.find_all("tr"):
# 	if d.find("td")!=None:
# 		print(d.find("td",{"class":"only_web"}).text,d.find("td").text)

# 抓出網址
# b=BeautifulSoup(r.text,"html.parser")
# for d in b.find_all("tr"):
# 	if d.find("td")!=None:
# 		print(d.find("td",{"class":"only_web"}).text,d.find("td").text,d.find("td").find("a").attrs["href"])

# 抓出所有新聞內容並存檔
# b=BeautifulSoup(r.text,"html.parser")
# fn=0
# for d in b.find_all("tr"):
# 	if d.find("td")!=None:
# 		category=d.find("td",{"class":"only_web"}).text
# 		title=d.find("td").text
# 		url=d.find("td").find("a").attrs["href"]
# 		r2=requests.get(
# 			url,
# 			headers={
# 				"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
# 			}
# 		)
# 		b2=b=BeautifulSoup(r2.text,"html.parser")
# 		content=b2.find("div",{"id":"article_body"}).text
# 		fn+=1
# 		with codecs.open("news/"+str(fn)+".txt","w","utf8") as f:
# 			f.write(url+"\r\n")
# 			f.write(category+"\r\n")
# 			f.write(title+"\r\n")
# 			f.write(content+"\r\n")


# 抓取圖片
# b=BeautifulSoup(r.text,"html.parser")
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
# 				"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
# 			}
# 		)
# 		b2=b=BeautifulSoup(r2.text,"html.parser")
# 		content=b2.find("div",{"id":"article_body"}).text
# 		fn+=1

# 		with codecs.open("news/"+str(fn)+".txt","w","utf8") as f:
# 			f.write(url+"\r\n")
# 			f.write(category+"\r\n")
# 			f.write(title+"\r\n")
# 			f.write(content+"\r\n")
# 		for m in b2.find("div",{"id":"article_body"}).find_all("img"):
# 			r3=requests.get(
# 				m.attrs["src"],
# 				headers={
# 					"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
# 				}
# 			)
# 			img+=1
# 			with codecs.open("images/"+str(img)+".jpg","wb") as f:
# 				f.write(r3.content)


from bs4 import BeautifulSoup
r = requests.get(
	"https://www.taiwan.net.tw/m1.aspx",
	params={
		"sNo":"0001001"
	},
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

	}
)
b1=BeautifulSoup(r1.text, "html.parser")
for d1 in b1.find_all()