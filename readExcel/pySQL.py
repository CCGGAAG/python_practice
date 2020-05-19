import pymysql.cursors
# 连接数据库
def select(sqls):
    connect = pymysql.Connect(
        host='bdm278066426.my3w.com',
        port=3306,
        user='',
        passwd='',
        db='bdm278066426_db',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()
    # 查询数据
    sql = sqls
    try:
       # 执行SQL语句
       cursor.execute(sql)
       connect.commit()
    except:
       connect.rollback()
       print ("Error: unable to fetch data")
    # 关闭连接
    cursor.close()
    connect.close()

# if __name__ == '__main__':
#     select("")
