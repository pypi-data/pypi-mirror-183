import pymysql
import pandas as pd

def woojiniconnectDB(host1, user1, password1, db1, table_name, start_day, end_day):
    conn=pymysql.connect(host=host1, user=user1, password=password1, db=db1, charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    cur=conn.cursor()
    if db1=='fems':
        sql='select * from ' + table_name + '\' where time >= \'' + start_day + '\' and time <= \'' + end_day + '\';'
        cur.execute(sql)
        rows=cur.fetchall()
        conn.close()
        return pd.DataFrame(rows)
    elif db1=='vup':
        sql='select * from ' + table_name + ' where collected_dt >= \'' + start_day + '\' and collected_dt <= \'' + end_day + '\';'
        cur.execute(sql)
        rows=cur.fetchall()
        conn.close()
        return pd.DataFrame(rows)