import requests

r=requests.get(
	"http://teaching.bo-yuan.net/test/requests/",
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	},
	
)
r.encoding="utf8"
print(r.text)


r=requests.get(
	"http://teaching.bo-yuan.net/test/requests/",
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	},
	params={
	"action":" "
	}
	
)
r.encoding="utf8"
print(r.text)


r=requests.delete(
	"http://teaching.bo-yuan.net/test/requests/",
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	},
	params={
	"action":" "
	}
	
)
r.encoding="utf8"
print(r.text)


r=requests.delete(
	"http://teaching.bo-yuan.net/test/requests/",
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	},
	params={
	"action":" "
	},
	data={
	"id":"29"
	}
	
)
r.encoding="utf8"
print(r.text)



r=requests.put(
	"http://teaching.bo-yuan.net/test/requests/",
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	},
	params={
	"action":" "
	},
	data={
	"id":" "
	}
	
)
r.encoding="utf8"
print(r.text)



r=requests.put(
	"http://teaching.bo-yuan.net/test/requests/",
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	},
	params={
	"action":" "
	},
	data={
	"id":" ",
	"name":"林豈禾"
	}
	
)
r.encoding="utf8"
print(r.text)

r=requests.patch(
	"http://teaching.bo-yuan.net/test/requests/",
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	},
	params={
	"action":" "
	},
	data={
	"id":" ",
	"name":"林豈禾"
	}
	
)
r.encoding="utf8"
print(r.text)

r=requests.patch(
	"http://teaching.bo-yuan.net/test/requests/",
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	},
	params={
	"action":" "
	},
	data={
	"id":" ",
	"name":"林豈禾",
	"address":"123456"
	}
	
)
r.encoding="utf8"
print(r.text)

r=requests.post(
	"http://teaching.bo-yuan.net/test/requests/",
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
	"Cookie":"PHPSESSID=duopt4k25mbkksasj2fcern3k7"
	},
	params={
	"action":" "
	},
	data={
	"id":" ",
	"name":"林豈禾",
	"address":"123456"
	}
	
)
r.encoding="utf8"
print(r.text)