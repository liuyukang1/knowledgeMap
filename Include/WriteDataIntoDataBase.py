import pymysql

if __name__ == '__main__':
    conn=pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='000000',
        database='knowledgeMap',
        charset='utf8'
    ) #前提先启动mysql服务器

    #输出数据的时候,根据游标往后取值
    cursor = conn.cursor() #创建游标 mysql>

    mysql_cmd = "select * from announcement;" #命令语句str

    cursor.execute(mysql_cmd)  #执行命令行语句

    cursor.scroll(3,'absolute') #绝对路径游标往下跳过条数据

    print(cursor.fetchall()) #获取所有数据

