#!/usr/bin/python
import StatSquash.config as config
from StatSquash.helper import parse_args, query_value, get_avg

args = parse_args()
table = config.tables[args['interval']]
queryNum = query_value(table, 'total_posts', args['date'])
queryDenom = query_value(table, 'total_users', args['date'])
print get_avg(config.load_db, queryNum, queryDenom)   