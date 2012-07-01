import os.path
from dateutil.relativedelta import relativedelta
from StatSquash.helper import query_value, get_avg

class Avg:
    
    def __init__(self, db_params, tables, avg_from, new_prefix='avg_'):
        self.db_params = db_params
        self.tables = tables
        self.avg_from = avg_from
        self.new_prefix = new_prefix
        
    def farm(self, loader, start_date, end_date, interval):
        
        table = self.tables[interval]
        data = []
        for num_label, denom_label in self.avg_from:
                        
            cur_date = start_date
            while cur_date <= end_date:
                new_label = "".join([self.new_prefix, num_label])
                queryNum = query_value(table, num_label, cur_date - relativedelta(months=1))   
                queryDenom =query_value(table, denom_label, cur_date)
                avg = get_avg(self.db_params, queryNum, queryDenom)   
                data.append((new_label, avg, cur_date))
                cur_date = cur_date + relativedelta(months=1) 
     
        if len(data) > 0:
            loader.load(data)