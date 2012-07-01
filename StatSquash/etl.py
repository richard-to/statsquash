import os
import os.path
import subprocess
import MySQLdb

class Extractor:
    
    def __init__(self, whitelist=None):
        self.whitelist = whitelist
    def extract(self, location, start_date, today, interval):
        data = []
        if os.path.isfile(location):
            path, filename = os.path.split(location)
            label, ext = os.path.splitext(filename)
            if self.whitelist is None or label in self.whitelist:
                result = (subprocess.check_output([location, str(start_date), str(today), interval])).strip()
                data.append((label, result, today))                
        else:
            for dirname, dirnames, filenames in os.walk(location):
                for filename in filenames:
                    script = os.path.join(dirname, filename)
                    label, ext = os.path.splitext(filename)
                    if self.whitelist is None or label in self.whitelist:
                        result = (subprocess.check_output([script, str(start_date), str(today), interval])).strip()
                        data.append((label, result, today)) 
        return data
            
class Loader:
    
    def __init__(self, db_params, table):
        self.db_params = db_params
        self.table = table
        self.base_query = "insert into {} (label, value, created_at) values ".format(self.table)

    def load(self, rows):    
        query = ''.join([self.base_query, ", ".join("('%s', %s, '%s')" % row for row in rows)])

        conn = MySQLdb.connect(**self.db_params)        
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.close()
        conn.commit()        
        conn.close()