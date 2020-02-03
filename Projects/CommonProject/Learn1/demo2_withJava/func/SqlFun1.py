import pymysql


def insert1():
    conn = pymysql.connect(host='localhost',
                           port=5306,
                           user='root',
                           passwd='root',
                           db='db1',
                           charset='utf8')

    cur = conn.cursor()  # 获取游标，以操作数据库
    sql = """ insert into account(name,money) values('python',100) """
    cur.execute(sql)  # 执行sql语句
    conn.commit()  # 执行增、删、改操作时需要手动提交，否则不会修改到数据库中的数据！
    cur.close()
    conn.close()
    print('执行sqlFun1.py成功！')
