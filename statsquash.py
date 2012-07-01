#!/usr/bin/python

from datetime import date, timedelta
import StatSquash.config as config
from StatSquash.etl import Loader

settings = config.harvester
if config.dev == True:
    settings = config.harvester_dev
    
today = date.today()
farmland = settings['farmland']
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
    
loader = Loader(db, table)

for plot in farmland:
    plot.farm(loader, start_date, end_date, interval)