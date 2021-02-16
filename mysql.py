import pymysql
import json

def getData(tableName,*rowName):
    con = pymysql.connect(host='localhost', user='root', password='daluosiNB', database='test_daluosi', port=3309)
    sql=f'select {",".join(rowName)} from {tableName}'
    cur=con.cursor()
    cur.execute(sql)
    datas=cur.fetchall()
    ls=[]
    for  data in datas:
        d={}
        for i in enumerate(data):
            if rowName[i[0]]=='datetime':
                d[rowName[i[0]]]=json.dumps(i[0])
            else:
                d[rowName[i[0]]]=i[1]
        ls.append(d)
    return ls


def insert(data, tableName):
    con = pymysql.connect(host='localhost', user='root', password='daluosiNB', database='test_daluosi', port=3309)

    sql = f"""insert into {tableName}(username, datetime, diff, remark) values ('{data["username"]}','{data["datetime"]}','{data["diff"]}','{data["remark"]}');"""
    print(sql)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()


def get_max_id():
    con = pymysql.connect(host='localhost', user='root', password='daluosiNB', database='test_daluosi', port=3309)

    sql = f"""select id from make_group"""
    cur = con.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    con.close()
    return int(data[0][0])
