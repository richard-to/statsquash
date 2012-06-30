import sys
from datetime import datetime
import MySQLdb
from dateutil.relativedelta import relativedelta

def get_last_month_date(str_date):
    cur_date = datetime.strptime(str_date, '%Y-%m-%d')
    return cur_date - relativedelta(months=1)
    
def parse_args():
    args = {}
    if len(sys.argv) == 3:
        args['date'] = sys.argv[1]
        args['interval'] = sys.argv[2]
    else:
        sys.exit()
    return args

def query_value(table, label, cur_date):
    return ("select value from {} "
        "where label = '{}' and created_at = '{} 00:00:00' limit 1"
        "").format(table, label, cur_date)
 
def get_result(db_params, query):
    data = fetch_one(db_params, query)
    result = 0
    if data != None:
        result = data[0]
    return result  

def get_avg(db_params, queryNum, queryDenom):
    num = fetch_one(db_params, queryNum)
    denom = fetch_one(db_params, queryDenom)
    avg = 0
    if(denom[0] != 0):
        avg = num[0]/denom[0]    
    return avg   
                            
def fetch_one(db_params, query):
    conn = MySQLdb.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data