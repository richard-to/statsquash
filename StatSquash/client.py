import MySQLdb

class GrapherChef:
    
    def __init__(self, harvester, style):
        self.harvester = harvester
        self.style = style
    
    def cook(self, recipes):
        graphs = []
        self.harvester.start()
        for recipe in recipes:
            point_set = [self.harvester.harvest(label) for label in recipe['data']]
            graphs.append(self.style.prepare(
                recipe['title'], recipe['type'], recipe['headers'], point_set))
        self.harvester.finish()        
        return graphs
    
class MySqlHarvester:
    
    def __init__(self, db_params, table):
        self.db_params = db_params
        self.table = table
        self.conn = None
        
    def start(self):
        self.conn = MySQLdb.connect(**self.db_params)    
                
    def harvest(self, label):
        
        query = ("select date_format(created_at, '%%b %%Y'), label, value from %s "
        "where label = '%s' order by created_at asc"
        "") % (self.table, label)
        
        cursor = self.conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

        return data
    
    def finish(self):
        self.conn.close()
        
class GoogleChartStyle:
    
    def prepare(self, title, type, headers, point_set):
        data_array = "".join(['[', self.prepare_header(headers), self.prepare_points(point_set), ']'])
        return {'title':title, 'type':type, 'data':data_array}
    
    def prepare_header(self, headers):
        return "".join(['[' ,", ".join("'%s'" % header for header in headers), '],'])
    
    def prepare_points(self, point_set):
        cols = len(point_set)
        rows = []
        for i in range(len(point_set[0])):
            row = ["".join(["'",point_set[0][i][0],"'"])]
            row.extend([point_set[col][i][2] for col in range(cols)])
            rows.append(row)
        template = "".join(["[", ",".join("%s" for col in range(cols+1)), "]"])
        return ",".join(template % tuple(row) for row in rows)
 