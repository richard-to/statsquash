import sys
import math
from datetime import datetime
import MySQLdb
from dateutil.relativedelta import relativedelta

def get_last_month_date(str_date):
    return sub_month_date(str_date)

def sub_month_date(str_date, sub_months=1):
    cur_date = datetime.strptime(str_date, '%Y-%m-%d')
    return cur_date - relativedelta(months=sub_months)
    
def parse_args():
    args = {}
    if len(sys.argv) == 4:
        args['start_date'] = sys.argv[1]        
        args['end_date'] = sys.argv[2]
        args['interval'] = sys.argv[3]
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
    if data != None and data[0] != None:
        result = data[0]
    return result  

def get_avg(db_params, queryNum, queryDenom):
    num = fetch_one(db_params, queryNum)
    denom = fetch_one(db_params, queryDenom)
    avg = 0
    if num != None and denom != None and denom[0] != 0:
        avg = num[0]/denom[0]    
    return avg   

def get_pct(db_params, queryNum, queryDenom):
    num = fetch_one(db_params, queryNum)
    denom = fetch_one(db_params, queryDenom)
    pct = 0

    if num != None and denom != None and denom[0] != 0:
        pct = math.ceil(((float(num[0])/float(denom[0]))*100))  
    return pct
                               
def fetch_one(db_params, query):
    conn = MySQLdb.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    conn.close()

    if data != None:
        data = [0 if val is None else val for val in data]
        
    return data