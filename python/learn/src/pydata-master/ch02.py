'''
Created on Jul 19, 2016

@author: airings
'''

import json
path = "/Users/airings/Programming/python/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt"

# print open(path).readline()

records = [json.loads(line) for line in open(path)]

print records[0]