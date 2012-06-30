#!/usr/bin/python
import StatSquash.config as config
from StatSquash.helper import parse_args, get_result

args = parse_args()
query = ("select count(*) from users where created_at <= '{}'").format(args['date'])
print get_result(config.extract_db, query)