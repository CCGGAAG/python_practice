#说明:
	#这个代码是拉勾网爬虫

#依赖
	#pip3 install requests
	#pip3 install pymysql
	#pip3 install pyquery

#执行方式
#		python3 lagou.py                                                                                                           
	


#建表的指令
'''
CREATE TABLE `job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `companyId` bigint(4) DEFAULT NULL,
  `positionName` varchar(64) DEFAULT NULL,
  `workYear` varchar(16) DEFAULT NULL,
  `education` varchar(16) DEFAULT NULL,
  `jobNature` varchar(16) DEFAULT NULL,
  `positionId` bigint(4) DEFAULT NULL,
  `companyShortName` varchar(16) DEFAULT NULL,
  `createTime` varchar(38) DEFAULT NULL,
  `score` bigint(4) DEFAULT NULL,
  `city` varchar(16) DEFAULT NULL,
  `salary` varchar(16) DEFAULT NULL,
  `approve` bigint(4) DEFAULT NULL,
  `positionAdvantage` varchar(128) DEFAULT NULL,
  `financeStage` varchar(16) DEFAULT NULL,
  `industryField` varchar(16) DEFAULT NULL,
  `companySize` varchar(18) DEFAULT NULL,
  `companyLabelList` varchar(128) DEFAULT NULL,
  `publisherId` bigint(4) DEFAULT NULL,
  `district` varchar(16) DEFAULT NULL,
  `companyLogo` varchar(106) DEFAULT NULL,
  `positionLables` varchar(128) DEFAULT NULL,
  `industryLables` varchar(128) DEFAULT NULL,
  `businessZones` varchar(128) DEFAULT NULL,
  `hitags` varchar(128) DEFAULT NULL,
  `resumeProcessRate` bigint(4) DEFAULT NULL,
  `resumeProcessDay` bigint(4) DEFAULT NULL,
  `companyFullName` varchar(28) DEFAULT NULL,
  `imState` varchar(16) DEFAULT NULL,
  `lastLogin` bigint(4) DEFAULT NULL,
  `explain` varchar(128) DEFAULT NULL,
  `adWord` bigint(4) DEFAULT NULL,
  `plus` varchar(128) DEFAULT NULL,
  `pcShow` bigint(4) DEFAULT NULL,
  `appShow` bigint(4) DEFAULT NULL,
  `deliver` bigint(4) DEFAULT NULL,
  `gradeDescription` varchar(128) DEFAULT NULL,
  `promotionScoreExplain` varchar(128) DEFAULT NULL,
  `firstType` varchar(16) DEFAULT NULL,
  `secondType` varchar(16) DEFAULT NULL,
  `isSchoolJob` bigint(4) DEFAULT NULL,
  `subwayline` varchar(16) DEFAULT NULL,
  `stationname` varchar(16) DEFAULT NULL,
  `linestaion` varchar(256) DEFAULT NULL,
  `longitude` varchar(20) DEFAULT NULL,
  `latitude` varchar(18) DEFAULT NULL,
  `formatCreateTime` varchar(16) DEFAULT NULL,
  `advantage` text,
  `describe` text,
  `address` text,
  `lagou_src` varchar(128) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8;

'''

#导入需要的库 - 标准库
import re       #本模块提供了类似于Perl的正则表达式匹配操作。要匹配的模式和字符串可以是Unicode字符串以及8位字符串。
from lxml import etree	#通过xpath语法获取数据
import time #用于重复
import hashlib	#导入md5
import traceback 
import math
import json

#导入需要的库 - 第三方库
import requests #用于请求数据
import pymysql  #导入pymysql, 用于数据库操作
#import pyquery
from pyquery import PyQuery as pq


#请求头
headers = {'cookie': 'WEBTJ-ID=20180416170315-162cdb1aa283a2-09bcc09c09dd55-173f6d56-1024000-162cdb1aa294b0; user_trace_token=20180416170315-ffcb35e2-4154-11e8-8778-525400f775ce; LGUID=20180416170315-ffcb3c5a-4154-11e8-8778-525400f775ce; X_HTTP_TOKEN=f652a4874439a91419793892f79023a3; LG_LOGIN_USER_ID=c68837a6202db61ccc00196c20a861cdbde851eaeeea42f9; _putrc=349A13C44D445C65; JSESSIONID=ABAAABAAAGGABCB6A4C3D4F1603307A5BCCD95129B93B6F; login=true; unick=%E5%BC%A0%E5%81%A5; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=9269072b150bfd7fcaa3695a648c3ba18791706668181872; TG-TRACK-CODE=jobs_code; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523869396,1524017613; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524019907; LGSID=20180418101330-16b8c5d9-42ae-11e8-89d3-525400f775ce; LGRID=20180418105147-6f856265-42b3-11e8-89d5-525400f775ce; _ga=GA1.2.2080449532.1523869396; _gid=GA1.2.224531527.1524017613; SEARCH_ID=0fab5891b480402eb5a37cfcf703b1fe; index_location_city=%E5%8C%97%E4%BA%AC',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
		'Referer':'https://www.lagou.com/jobs/list_%E4%BC%9A%E8%AE%A1?labelWords=&fromSearch=true&suginput='}

#图片存放位置
img_dir = "upload_company/temp/"

#页数定义: 在get_list_page()使用
page_start = 8
page_max = 30




db_host = "localhost"
db_user = "root"
#此处的密码为了安全因素没写, 请在使用的时候采用自己的密码
db_password = ""
db_name = "zhtest"
db_port = 3306
db_charset = 'utf8'


#Step1: 
#功能: 从数据表中获取所有企业的名单
#	注意: 依赖全局定义的数据库信息
def connet_database():
	
	db = pymysql.connect(host=db_host,user=db_user,
	    password=db_password,db=db_name,port=db_port,charset = db_charset)
	print(db)
	return db
pass

#执行连接数据库代码
db = connet_database()
# 使用cursor()方法获取操作游标  
cursor = db.cursor()
print("数据库连接成功!")

#根据table_name,row创建表
def create_table(table_name,row):

	sql = "create table job("
	sql += "id int auto_increment primary key,"
	index=0
	for key in row.keys():
		v_len = 4
		#print("key = "+key+"t="+str(type(row[key]))+" v="+str(row[key]))
		if(str(type(row[key])) == "<class 'int'>"):
			v_len = 4
			sql += "`"+key+"`" + " bigint("+str(v_len)+")"
		elif(str(type(row[key])) == "<class 'str'>"):
			v_len = len(row[key])*2
			if v_len<16:
				v_len = 16
			sql += "`"+key+"`" + " varchar("+str(v_len)+")"
		elif(str(type(row[key])) == "<class 'NoneType'>"):
			v_len = 128
			sql += "`"+key+"`" + " varchar("+str(v_len)+")"
		elif(str(type(row[key])) == "<class 'list'>"):
			v_len = 128	
			sql += "`"+key+"`" + " varchar("+str(v_len)+")"
		else:
			v_len = 64	
			sql += "`"+key+"`" + " varchar("+str(v_len)+")"

		if index != len(row)-1:
			sql += ","

		index+=1
		pass

	sql = sql+")"
	print("sql = "+sql)

	effect_row = cursor.execute(sql)
	#提交修改, 否则数据不会生效
	db.commit()

	return effect_row

	pass

#根据table_name,row插入数据
def insert_row(table_name,row):

	sql = "insert into "+table_name+"("
	index=0
	for key in row.keys():

		sql += "`"+key+"`"
		if(index != len(row)-1):
			sql += ","

		index+=1
		pass


	sql += ") values("


	index = 0
	for key in row.keys():
		value = str(row[key])
		value = value.replace("'","\\'")
		sql += "'"+value+"'"
		if(index != len(row)-1):
			sql += ","

		index+=1
		pass
	sql += ")"

	print("sql = "+sql)

	effect_row = cursor.execute(sql)
	#提交修改, 否则数据不会生效
	db.commit()

	return effect_row

	pass

#根据table_name,row,where更新表
def update_row(table_name,row,where):

	sql = "update "+table_name+""
	sql += " set "
	index=0
	for key in row.keys():
		value = str(row[key])
		value = value.replace("'","\\'")
		sql += "`"+key+"`='"+value+"'"
		if(index != len(row)-1):
			sql += ","

		index+=1
		pass

	if(where != ""):
		sql += " where "+where

	#print("sql = "+sql)

	effect_row = cursor.execute(sql)
	#提交修改, 否则数据不会生效
	db.commit()

	return effect_row

	pass

#根据table_name,row,where更新表
def delete_row(table_name,where):

	sql = "delete from "+table_name+""
	if(where != ""):
		sql += " where "+where

	print("sql = "+sql)


	effect_row = cursor.execute(sql)
	#提交修改, 否则数据不会生效
	db.commit()

	return effect_row

	pass

#根据table_name,row,where,other获取一条数据
def fetch_row(table_name,colum_list,where,other):

	#sql
	sql = "select "+colum_list+" from "+table_name
	if(where != ""):
		sql += " where "+where
	if(other != ""):
		sql += " "+other
	print("sql = "+sql)
	cursor.execute(sql)

	# 获取所有记录列表
	rows = cursor.fetchall()

	if(len(rows)>0):
		return rows[0]

	return None
	pass

#根据table_name,row,where,other获取多条数据
def fetch_all_row(table_name,colum_list,where,other):

	#sql
	sql = "select "+colum_list+" from "+table_name
	if(where != ""):
		sql += " where "+where
	if(other != ""):
		sql += " "+other
	print("sql = "+sql)
	cursor.execute(sql)

	# 获取所有记录列表
	rows = cursor.fetchall()

	return rows
	pass


def is_exist_row(table_name,where):

	sql = "select * from "+table_name
	if(where != ""):
		sql += " where "+where

	cursor.execute(sql)
	rows = cursor.fetchall()
	if(len(rows)>0):
		return True
	else:
		return False

	pass

#=============================================

#https://www.lagou.com/jobs/4399966.html
def get_detail_page(job_id):

	

	job_url = "https://www.lagou.com/jobs/"+str(job_id)+".html"
	print("job_url = "+str(job_url))
	params = {

	}
	response = requests.get(job_url,headers=headers)
	print("job页面大小 = "+str(len(response.text)))
	doc = pq(response.text)

	text1 = doc(".job-advantage>p").text()
	print("优势: "+text1)

	text2 = doc(".job_bt>div").text()
	#text2 = text2.replace("\u00a0","<br>")
	text2 = text2.replace("\n","<br>")
	print("描述: "+text2)


	text3 = doc(".work_addr").text()
	text3 = text3.replace("查看地图","").strip()
	print("地址: "+text3)


	row = {
		"advantage":text1,
		"describe":text2,
		"address":text3,
		"lagou_src":job_url
	}
	update_row("job",row,"positionId="+str(job_id))

	

	pass


def get_list_page():

	
	for p in range(page_start,page_max+1):

		#北京 - 会计
		list_url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
		#全国 - 会计
		list_url = "https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false"


		params = {
			"first":"false",
			"pn":p,
			"kd":"会计"
		}
		response = requests.post(list_url,data=params,headers=headers)
		print(response.text)

		json_dict = json.loads(response.text)
		total_count = json_dict['content']['positionResult']['totalCount']
		print("total_count = "+str(total_count))
		result = json_dict['content']['positionResult']['result']
		print("len = "+str(len(result)))

		job_index = 0
		for job in result:
			print("positionName = "+job['positionName'])
			#print(job.keys())

			'''
			job['advantage'] = ""
			job['describe'] = ""
			job['address'] = ""
			job['lagou_src'] = ""
			create_table("job",job)
			insert_row("job",job)
			insert_row("job",job)
			insert_row("job",job)
			update_row("job",job,"id = 1")
			delete_row("job","id = 1")
			row = fetch_row("job","positionName","id=1","")
			print("row = "+str(row))
			rows = fetch_all_row("job","positionName","","")
			print("rows = "+str(rows))
			'''

			
			job_id = job['positionId']

			print("======job start=======")
			print("当前页 p="+str(p))
			print("当前序号 job_index="+str(job_index))

			#如果不存在
			b = is_exist_row("job","positionId = "+str(job_id))
			if(not b):
				insert_row("job",job)
				get_detail_page(job_id)

				#每次爬取一页, 暂停1s
				time.sleep(1)

			else:
				print("数据已经存在")

			print("======job end=======")

			
			job_index+=1
			pass

		#暂时执行一次
		#break	#for结束

		#每一页, 1s暂停
		time.sleep(1)

	pass 	#函数结束


get_list_page()




