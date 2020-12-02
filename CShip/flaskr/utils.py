import pymysql

def get_conn():
    # 创建连接
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='20051104',
        db='django_StudenManage',
        charset='utf8', )
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组展示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    # 封装通用查询
    #:param sql:
    #:param args:
    #:return:返回查询结果，((),(),)的形式

    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def get_data():
    sql = "select brigade,ended_at from system_ste_output where if_average_br = 1"

    res = query(sql)
    return res
print(get_data())
