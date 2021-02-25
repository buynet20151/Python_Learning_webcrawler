import pymysql

link=pymysql.connect(
	host="localhost",
	user="root",
	passwd="",
	db="my",
	charset="utf8"
)

cur=link.cursor()

# title=input("標題 :")
# url=input("網址 :")
# description=input("描述 :")
# create_time=input("日期 :")
# source=input("來源 :")

# cur.execute(
# 	"INSERT INTO `news`(`title`,`url`,`description`,`create_time`,`source`)"+
# 	"VALUES(%s,%s,%s,%s,%s)",
# 	[title,url,description,create_time,source]
# )
#List形式--------------------------------------------------------------------
# param=[
# 	input("標題 :"),
# 	input("網址 :"),
# 	input("描述 :"),
# 	input("日期 :"),
# 	input("來源 :")
# 	]
# cur.execute(
# 	"INSERT INTO `news`(`title`,`url`,`description`,`create_time`,`source`)"+
# 	"VALUES(%s,%s,%s,%s,%s)",
# 	param
# )
#------------------------------------------------------------
#字典形式-----------------------------------------------------------------
param={
	"title":input("標題 :"),
	"url":input("網址 :"),
	"description":input("描述 :"),
	"create_time":input("日期 :"),
	"source":input("來源 :")
	}
cur.execute(
	"INSERT INTO `news`(`title`,`url`,`description`,`create_time`,`source`)"+
	"VALUES(%(title)s,%(url)s,%(description)s,%(create_time)s,%(source)s)",
	param
)
#---------------------------------------------------------------------------
#字典修改------------------------------------
# param={
# 	"id":input("要修改的ID :"),
# 	"title":input("標題 :"),
# 	"url":input("網址 :")
# }
# cur.execute(
# 	"UPDATE `news` SET `title`=%(title)s,`url`=%(url)s"+
# 	"WHERE `id`=%(id)s",
# 	param
# )
#--------------------------------------------------------

#-----------------------------------------
# cur.execute("SELECT * FROM `news`")
# # ret=cur.fetchall()
# # for d in ret:
# # 	print(d[0],d[1],d[2])

# d=cur.fetchone()
# print(d[0],d[1],d[2])
# d=cur.fetchone()
# print(d[0],d[1],d[2])

# ret=cur.fetchall()
# for d in ret:
# 	print(d[0],d[1],d[2])
# print("總共資料筆數 : ",cur.rowcount)


# link.close()
#------------------------------------------------

# param={
# 	"title":input("標題 :"),
# 	"url":input("網址 :"),
# 	"description":input("描述 :"),
# 	"create_time":input("日期 :"),
# 	"source":input("來源 :")
# 	}
# cur.execute(
# 	"INSERT INTO `news`(`title`,`url`,`description`,`create_time`,`source`)"+
# 	"VALUES(%(title)s,%(url)s,%(description)s,%(create_time)s,%(source)s)",
# 	param
# )
# link.commit()
# newid=cur.lastrowid
# print("剛剛新增那筆資料的ID : ",newid)
#------------------------------------------------------
import prettytable
p=prettytable.PrettyTable(["ID","Title"],encoding="utf8")

cur.execute("SELECT * FROM `news`")

ret=cur.fetchall()
for d in ret:
	p.add_row([d[0],d[1]])
print(p)


link.close()

