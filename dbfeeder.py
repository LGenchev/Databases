#learning sqlite
import sqlite3
import pandas as pd
import csv

conn=sqlite3.connect('mktdata.db')
c=conn.cursor()
# c.execute('''CREATE TABLE ohlcSPX (Date text, Open float, High float,Low float, Close float, AdjClose float,Volume int )''')
# c.execute('''CREATE TABLE ohlcSPX (Date text, Open text, High text,Low text, Close text, AdjClose text,Volume text )''')

with open('ohlc_SP500.csv','rb') as csvfile:
	data=csv.DictReader(csvfile)
	to_db=[(i.values()) for i in data]
c.executemany("INSERT INTO ohlcSPX(Date,Open,High,Low,Close,AdjClose,Volume) VALUES (?,?,?,?,?,?,?);",to_db)

for row in c.execute("SELECT * FROM ohlcSPX WHERE Open>2600;"):
	print(row)
conn.commit()
conn.close()

