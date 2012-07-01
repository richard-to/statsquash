from dateutil.relativedelta import relativedelta

class Planter:
    
    def __init__(self, extractor, location):
        self.location = location
        self.extractor = extractor
        
    def farm(self, loader, start_date, end_date, interval):
        
        data = []
        cur_date = start_date
        
        while cur_date <= end_date:
            data.extend(self.extractor.extract(self.location, start_date, cur_date, interval))
            cur_date = cur_date + relativedelta(months=1) 
            
        if len(data) > 0:
            loader.load(data)