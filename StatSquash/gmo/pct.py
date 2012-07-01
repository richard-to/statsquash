import os.path
from dateutil.relativedelta import relativedelta
from StatSquash.helper import query_value, get_pct

class Pct:
    
    def __init__(self, db_params, tables, pct_from, new_prefix='pct_'):
        self.db_params = db_params
        self.tables = tables
        self.pct_from = pct_from
        self.new_prefix = new_prefix
        
    def farm(self, loader, start_date, end_date, interval):
        
        table = self.tables[interval]
        data = []
        for num_label, denom_label in self.pct_from:
                        
            cur_date = start_date
            while cur_date <= end_date:
                new_label = "".join([self.new_prefix, num_label])
                queryNum = query_value(table, num_label, cur_date - relativedelta(months=1))   
                queryDenom =query_value(table, denom_label, cur_date)
                pct = get_pct(self.db_params, queryNum, queryDenom)   
                data.append((new_label, pct, cur_date))
                cur_date = cur_date + relativedelta(months=1) 
     
        if len(data) > 0:
            loader.load(data)