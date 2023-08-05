import pymysql
import pandas as pd


def iae_db_connect(*argv):
    conn = pymysql.connect(host=argv[0], user=argv[1], password=argv[2], db=argv[3], charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    if argv[3] == 'fems':
        if len(argv) == 7:
            sql = 'select * from ' + argv[4] + ' where time >= \'' + argv[5] + '\' and time <= \'' + argv[6] + '\';'
            cur.execute(sql)
            rows = cur.fetchall()
            conn.close()
            return pd.DataFrame(rows)
        else:
            sql = 'select * from ' + argv[4] + ';'
            cur.execute(sql)
            rows = cur.fetchall()
            conn.close()
            return pd.DataFrame(rows)
    elif argv[3] == 'vup':
        if len(argv) == 7:
            sql = 'select * from ' + argv[4] + ' where collected_dt >= \'' + argv[5] + '\' and collected_dt <= \'' + \
                  argv[6] + '\';'
            cur.execute(sql)
            rows = cur.fetchall()
            conn.close()
            return pd.DataFrame(rows)
        else:
            sql = 'select * from ' + argv[4] + ';'
            cur.execute(sql)
            rows = cur.fetchall()
            conn.close()


def vup_db_connector(*argv):
    conn = pymysql.connect(host='192.168.3.125', user=argv[1], password=argv[2], db=argv[3], charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    if len(argv) == 6:
        sql = 'select * from ' + argv[4] + ' where collected_dt >= \'' + argv[5] + '\' and collected_dt <= \'' + \
              argv[6] + '\';'
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return pd.DataFrame(rows)
    else:
        sql = 'select * from ' + argv[4] + ';'
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return pd.DataFrame(rows)


def fems_db_connector(*argv):
    conn = pymysql.connect(host='192.168.3.128', user=argv[1], password=argv[2], db=argv[3], charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    if len(argv) == 6:
        sql = 'select * from ' + argv[4] + ' where time >= \'' + argv[5] + '\' and time <= \'' + argv[6] + '\';'
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return pd.DataFrame(rows)
    else:
        sql = 'select * from ' + argv[4] + ';'
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return pd.DataFrame(rows)
