# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:14:56 2019

"""

import sqlite3

def convert(value):
    if value.startwith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE food(
id        TEXT      PRIMARY KEY,
desc      TEXT,
water     FLOAT,
kcal      FLOAT,
protein   FLOAT,
fat       FLOAT,
ash       FLOAT,
carbs     FLOAT,
fiber     FLOAT,
suger     FLOAT
)             
''')

query = 'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?)'

for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()

'''------------next  code----------------------'''
import sqlite3, sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE %s' % sys.argv[1]

curs.execute(query)

names = [f[0] for f in curs.description] # description结果列描述的序列
for row in curs.fetchall():  # 提取结果
    for pair in zip(names, row):
        print('%s: %s' % pair)
