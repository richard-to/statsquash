import os
import os.path
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import MySQLdb
from StatSquash.helper import query_value, get_result, fetch_one

class Change:
    
    def __init__(self, db_params, tables, find_prefix='total_', replace_prefix='change_'):
        self.db_params = db_params
        self.tables = tables
        self.find_prefix = find_prefix
        self.replace_prefix = replace_prefix
        
    def run(self, loader, location, start_date, end_date, interval):
        
        labels = []
        if os.path.isfile(location):
            path, filename = os.path.split(location)
            label, ext = os.path.splitext(filename)
            
            if label.startswith(self.find_prefix):
                new_label = label.replace(self.find_prefix, self.replace_prefix)
                labels.append((label, new_label))             
        else:
            for dirname, dirnames, filenames in os.walk(location):
                for filename in filenames:
                    script = os.path.join(dirname, filename)
                    label, ext = os.path.splitext(filename)

                    if label.startswith(self.find_prefix):
                        new_label = label.replace(self.find_prefix, self.replace_prefix)
                        labels.append((label, new_label))  
        
        table = self.tables[interval]    
        data = []         
        for label, new_label in labels:    
            cur_date = start_date
            while cur_date <= end_date:
                val1 = get_result(self.db_params, query_value(table, label, cur_date - relativedelta(months=1)))    
                val2 = get_result(self.db_params, query_value(table, label, cur_date))    
                data.append((new_label, val2-val1, cur_date))
                cur_date = cur_date + relativedelta(months=1) 
     
        if len(data) > 0:
            loader.load(data)