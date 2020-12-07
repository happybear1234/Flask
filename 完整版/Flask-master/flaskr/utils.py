import pymysql

def get_conn():
    # 创建连接
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='newest data',
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

# 单一舰队使用可用度数据提取
def get_t11_data():
    # brigade = request.form.get('select1')
    sql = "select brigade,availability_sta_op,started_at,ended_at from system_ste_output where if_average_br = 1"

    res = query(sql)
    return res
# 单一舰队使用可用度图1数据传输
def t11(br, s, e):
    res = []
    brigade = br
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t11_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == brigade:
            res.append({"name": i[0], "value": i[1]})
    return res

# 单一舰队使用可用度图1数据传输
def t12(s, e):
    res = []
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t11_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end):
            res.append({"name": i[0], "value": i[1]})
    return res

# 单一舰队年度使用可用度数据传输
def t13(br, s, e):
    res = []
    brigade = br
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t11_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[2].split(".")[0]) <= int(end) and i[0] == brigade:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一试验固有可用度数据提取
def get_t21_data():
    # brigade = request.form.get('select1')
    sql = "select system,availability_sta_op,started_at,ended_at from system_ste_output where if_average_hybird = 1"

    res = query(sql)
    return res

# 单一系统使用可用度
def t21(sy, s, e):
    res = []
    system = sy
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t21_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == system:
            res.append({"name": i[0], "value": i[1]})
    return res

# 所有系统使用可用度
def t22(s, e):
    res = []
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t21_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end):
            res.append({"name": i[0], "value": i[1]})
    return res

# 单一系统年度使用可用度
def t23(sy, s, e):
    res = []
    system = sy
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t21_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[2].split(".")[0]) <= int(end) and i[0] == system:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res


# 单一试验固有可用度数据提取
def get_t31_data():
    # brigade = request.form.get('select1')
    sql = "select experiment,availability_sta,started_at,ended_at from system_ste_output where if_average_ex = 1"

    res = query(sql)
    return res

# 单一试验固有可用度
def t31(ex, s, e):
    res = []
    experiment = ex
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t31_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == experiment:
            res.append({"name": i[0], "value": i[1]})
    return res

# 所有试验固有可用度
def t32(s, e):
    res = []
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t31_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end):
            res.append({"name": i[0], "value": i[1]})
    return res

# 单一试验年度固有可用度
def t33(ex, s, e):
    res = []
    experiment = ex
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t31_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[2].split(".")[0]) <= int(end) and i[0] == experiment:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一系统马氏稳态可用度中舰队
def get_t41_data():
    # brigade = request.form.get('select1')
    sql = "select brigade,availability_mod,started_at,ended_at from system_ste_output where if_average_br = 1"

    res = query(sql)
    return res

def t411(br, s, e):
    res = []
    brigade = br
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t41_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == brigade:
            res.append({"name": i[0], "value": i[1]})
    return res

def t412(s, e):
    res = []
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t41_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end):
            res.append({"name": i[0], "value": i[1]})
    return res

# 单一系统马氏稳态可用度中系统
def get_t42_data():
    sql = "select system,availability_mod,started_at,ended_at from system_ste_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t421(sy, s, e):
    res = []
    system = sy
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t31_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == system:
            res.append({"name": i[0], "value": i[1]})
    return res

def t422(s, e):
    res = []
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t42_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end):
            res.append({"name": i[0], "value": i[1]})
    return res

# 单一系统马氏稳态可用度中试验
def get_t43_data():
    sql = "select experiment,availability_mod,started_at,ended_at from system_ste_output where if_average_ex = 1"
    res = query(sql)
    return res

def t431(ex, s, e):
    res = []
    experiment = ex
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t43_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == experiment:
            res.append({"name": i[0], "value": i[1]})
    return res

def t432(s, e):
    res = []
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t43_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end):
            res.append({"name": i[0], "value": i[1]})
    return res

# 单一系统瞬时可用度中舰队
def get_t44_data():
    sql = "select brigade,availability,started_at,ended_at,times from system_ins_output where if_average_br = 1"
    res = query(sql)
    return res

def t441(s, e):
    res = []
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t44_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end):
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统瞬时可用度中系统
def get_t45_data():
    sql = "select system ,availability,started_at,ended_at,times from system_ins_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t451(s, e):
    res = []
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t45_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end):
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统瞬时可用度中试验
def get_t46_data():
    sql = "select experiment,availability,started_at,ended_at,times from system_ins_output where if_average_ex = 1"
    res = query(sql)
    return res

def t461(s, e):
    res = []
    start = s.split("-")[0]
    end = e.split("-")[0]
    for i in get_t46_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end):
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统所有设备MTBF中舰队
def get_t51_data():
    sql = "select brigade,MTBF,start_time,end_time,device from part_output where if_average_br = 1"
    res = query(sql)
    return res

def t511(br, s, e):
    res = []
    brigade = br
    start = s
    end = e
    for i in get_t51_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == brigade:
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统所有设备MTBF中系统
def get_t52_data():
    sql = "select system,MTBF,start_time,end_time,device from part_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t521(sy, s, e):
    res = []
    system = sy
    start = s
    end = e
    for i in get_t52_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == system:
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统所有设备MTBF中试验
def get_t53_data():
    sql = "select experiment,MTBF,start_time,end_time,device from part_output where if_average_ex = 1"
    res = query(sql)
    return res

def t531(ex, s, e):
    res = []
    experiment = ex
    start = s
    end = e
    for i in get_t53_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == experiment:
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统单一设备年度MTBF中舰队
def get_t61_data():
    sql = "select brigade,MTBF,start_time,end_time,device from part_output where if_average_br = 1"
    res = query(sql)
    return res

def t611(de, s, e):
    res = []
    device = de
    start = s
    end = e
    for i in get_t61_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[4] == device:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一系统单一设备年度MTBF中系统
def get_t62_data():
    sql = "select system,MTBF,start_time,end_time,device from part_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t621(de, s, e):
    res = []
    device = de
    start = s
    end = e
    for i in get_t62_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[4] == device:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一系统单一设备年度MTBF中试验
def get_t63_data():
    sql = "select experiment,MTBF,start_time,end_time,device from part_output where if_average_ex = 1"
    res = query(sql)
    return res

def t631(de, s, e):
    res = []
    device = de
    start = s
    end = e
    for i in get_t63_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[4] == device:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一系统所有设备MTTR中舰队
def get_t71_data():
    sql = "select brigade,MTTR,start_time,end_time,device from part_output where if_average_br = 1"
    res = query(sql)
    return res

def t711(br, s, e):
    res = []
    brigade = br
    start = s
    end = e
    for i in get_t71_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == brigade:
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统所有设备MTTR中系统
def get_t72_data():
    sql = "select system,MTTR,start_time,end_time,device from part_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t721(sy, s, e):
    res = []
    system = sy
    start = s
    end = e
    for i in get_t72_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == system:
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统所有设备MTTR中试验
def get_t73_data():
    sql = "select experiment,MTTR,start_time,end_time,device from part_output where if_average_ex = 1"
    res = query(sql)
    return res

def t731(ex, s, e):
    res = []
    experiment = ex
    start = s
    end = e
    for i in get_t73_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == experiment:
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统单一设备年度MTTR中舰队
def get_t81_data():
    sql = "select brigade,MTTR,start_time,end_time,device from part_output where if_average_br = 1"
    res = query(sql)
    return res

def t811(de, s, e):
    res = []
    device = de
    start = s
    end = e
    for i in get_t81_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[4] == device:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一系统单一设备年度MTTR中系统
def get_t82_data():
    sql = "select system,MTTR,start_time,end_time,device from part_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t821(de, s, e):
    res = []
    device = de
    start = s
    end = e
    for i in get_t82_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[4] == device:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一系统单一设备年度MTTR中试验
def get_t83_data():
    sql = "select system,MTTR,start_time,end_time,device from part_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t831(de, s, e):
    res = []
    device = de
    start = s
    end = e
    for i in get_t83_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[4] == device:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一系统所有设备MDT中舰队
def get_t91_data():
    sql = "select brigade,MDT,start_time,end_time,device from part_output where if_average_br = 1"
    res = query(sql)
    return res

def t911(br, s, e):
    res = []
    brigade = br
    start = s
    end = e
    for i in get_t91_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == brigade:
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统所有设备MDT中系统
def get_t92_data():
    sql = "select system,MDT,start_time,end_time,device from part_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t921(sy, s, e):
    res = []
    system = sy
    start = s
    end = e
    for i in get_t92_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == system:
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统所有设备MDT中试验
def get_t93_data():
    sql = "select experiment,MDT,start_time,end_time,device from part_output where if_average_ex = 1"
    res = query(sql)
    return res

def t931(ex, s, e):
    res = []
    experiment = ex
    start = s
    end = e
    for i in get_t93_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[0] == experiment:
            res.append({"name": i[4], "value": i[1]})
    return res

# 单一系统单一设备年度MDT中舰队
def get_t101_data():
    sql = "select brigade,MDT,start_time,end_time,device from part_output where if_average_br = 1"
    res = query(sql)
    return res

def t1011(de, s, e):
    res = []
    device = de
    start = s
    end = e
    for i in get_t101_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[4] == device:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一系统单一设备年度MDT中系统
def get_t102_data():
    sql = "select system,MDT,start_time,end_time,device from part_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t1021(de, s, e):
    res = []
    device = de
    start = s
    end = e
    for i in get_t102_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[4] == device:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res

# 单一系统单一设备年度MDT中试验
def get_t103_data():
    sql = "select system,MDT,start_time,end_time,device from part_output where if_average_hybird = 1"
    res = query(sql)
    return res

def t1031(de, s, e):
    res = []
    device = de
    start = s
    end = e
    for i in get_t103_data():
        if int(i[2].split(".")[0]) >= int(start) and int(i[3].split(".")[0]) <= int(end) and i[4] == device:
            res.append({"name": i[2].split(".")[0], "value": i[1]})
    return res
