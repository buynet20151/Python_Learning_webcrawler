import flask
from flask import session
import time

# 讀取指定網址：
# 操作變數=flask.Flask(載入名稱, template_folder=模板路徑)
p1=flask.Flask("test", template_folder="C:/Users/ChiHe/Sublime_lesson/")
p1.config["SECRET_KEY"]=str(time.time())




x=0

# 設定網站頁面：
# @操作變數.route(網址路徑,methods=支援的方法, defaults=變數)
# def 函式名稱(網址路徑中的變數…):
@p1.route("/",methods=["GET","POST"])
def home():
	global x,session
	
	if "y" not in session:
		session["y"]=1
	else:
		session["y"]=int(session["y"])+1
	x+=1
	return flask.render_template("HTMLTRAINNING.html",x=x,y=session.get("y"))


@p1.route("/clear",methods=["GET"])
def clear():
	global x,session
	session.clear()
	return ""


# 載入網頁模板(return用)：
# flask.render_template(檔案位置, 變數1=…, 變數2=…, 變數345…)
@p1.route("/about",methods=["GET","POST"],defaults={"page":1})
@p1.route("/about/<int:page>",methods=["GET","POST"])
def about(page):
	return "PAGE="+str(page)


# 載入檔案(return用)：
# flask.send_from_directory(檔案路徑, 檔名, as_attachment=強制下載)
# @p1.route("/file",methods=["GET"])
# def file():
# 	return flask.send_from_directory("C:/Users/ChiHe/Sublime_lesson/images", "1.jpg", as_attachment=False)

@p1.route("/file",methods=["GET"],defaults={"filename":""})
@p1.route("/file/<string:filename>",methods=["GET"])
def file(filename):
	return flask.send_from_directory("C:/Users/ChiHe/Sublime_lesson/images", filename, as_attachment=False)

# 跳轉網址(return用)：
# flask.redirect(新位置)
@p1.route("/goto",methods=["GET"])
def goto():
	return flask.redirect("https://www.google.com/")


# 回傳內容(return用)：
# 操控變數=flask.make_response(要回傳的內容)
# 操控變數.headers=變數
# 操控變數.status_code=狀態代碼
@p1.route("/resp",methods=["GET"])
def resp():
	r=flask.make_response("ABC")
	r.headers={

	}
	r.status_code=404
	return r

# 取得網址參數
# flask.request.args.get(變數名稱, 預設值)
# flask.request.args.getlist(變數名稱)
@p1.route("/get",methods=["GET"])
def get():
	a=flask.request.args.get("q", "")
	b=flask.request.args.getlist("type")
	ret=""
	for d in b:
		ret+=str(d)+","

	return "q="+str(a)+"<br>type="+ret

# 取得資料變數：
# flask.request.form.get(變數名稱, 預設值)
# flask.request.form.getlist(變數名稱)
# 改成POST


# 取得檔案資料：
# flask.request.files[變數名稱].filename
#                             .save(路徑)



# 取得當前使用的方法(譬如GET, POST等等)：
# flask.request.method

# 可以把網頁中的敏感字元過濾掉：
# flask.escape(變數



# SESSION是網頁裡的一種可用於儲存資料的變數，讓每個使用者/瀏
# 覽器都可以有自己的獨立儲存空間

# 設定SESSION加密金鑰(字串型態)：
# 操作變數.config["SECRET_KEY"]=加密金鑰

# 設定SESSION變數：
# session["名稱"]=值

# 讀取SESSION變數：
# session["名稱"]
# session.get("名稱")


# 刪除SESSION變數：
# session.pop("名稱")

# 清空全部SESSION變數：
# session.clear()







# 啟動伺服器：
# 操作變數.run(host=主機名稱,port=網站Port)
p1.run(
	host="localhost",
	port=60
	)


