#!/usr/bin/python

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import StatSquash.config as config
from StatSquash.etl import Extractor, Loader

settings = config.harvester
if config.dev == True:
    settings = config.harvester_dev
    
today = date.today()
plugins = settings['plugins']
locations = settings['locations']
interval = settings['interval']
db = settings['db']
table = config.tables[interval]
start_date = settings['start_date']
end_date = settings['end_date']

if start_date == None:
    start_date = today

if end_date == None:
    end_date = today

if interval == 'monthly':
    start_date = start_date - timedelta(days=start_date.day-1)
    end_date = end_date - timedelta(days=end_date.day-1)    
    
extr = Extractor()
ldr = Loader(db, table)

for location in locations:
    data = []
    cur_date = start_date
    
    while cur_date <= end_date:
        data.extend(extr.extract(location, cur_date, interval))
        cur_date = cur_date + relativedelta(months=1) 
        
    if len(data) > 0:
        ldr.load(data)
    
    for plugin in plugins:
        plugin.run(ldr,location, start_date, end_date, interval)
