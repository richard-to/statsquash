from datetime import date
from StatSquash.plugins.change import Change

dev = False

extract_db = {
    'host':'',
    'user': '',
    'passwd': '',
    'db': ''
}

load_db = {
    'host':'',
    'user': '',
    'passwd': '',
    'db': ''
}

tables = {
    'monthly':'monthly_data'
}

data_dir = {
    'total': '/path/examples/queries/total',
    'avg': '/path/examples/queries/avg'
}

harvester = {
    'locations' : [
        data_dir['total'],
        data_dir['avg']
    ],
    'db': load_db,
    'interval': 'monthly',
    'start_date': date(2010, 10, 1),
    'end_date': date(2012, 6, 1),
    'plugins':[Change(load_db, tables)]    
}

harvester_dev = {
    'locations' : [
        data_dir['total'],
        data_dir['avg']
    ],
    'db': load_db,
    'interval': 'monthly',
    'start_date': date(2010, 10, 1),
    'end_date': date(2012, 6, 1),
    'plugins':[Change(load_db, tables)]    
}
