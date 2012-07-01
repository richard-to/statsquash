from dateutil.relativedelta import relativedelta

class QtrPlanter:
    
    def __init__(self, extractor, location, prefix='qtr_'):
        self.location = location
        self.extractor = extractor
        self.prefix = prefix
        
    def farm(self, loader, start_date, end_date, interval):
        
        data = []
        cur_date = start_date
        
        while cur_date <= end_date:
            qtr_date = cur_date - relativedelta(months=4)
            results = self.extractor.extract(self.location, qtr_date, cur_date, interval)
            for result in results:
                data.append(("".join([self.prefix, result[0]]), result[1], result[2]))
            cur_date = cur_date + relativedelta(months=1) 
            
        if len(data) > 0:
            loader.load(data)