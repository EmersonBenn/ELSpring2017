import os
import time
import sqlite3 as mydb
import sys

#readTime returns current date and time
def readTime():
	xdate = time.strftime('%Y-%m-%d')
	xtime = time.strftime('%H-%M-%S')
	return [xdate,xtime]

#logTime enters the current date and time into 2 column database testTime.db
def logTime():
	con = mydb.connect('testTime.db')
	with con:
		try:
			[d,t] = readTime()
			print [d,t]
			cur = con.cursor()
			cur.execute('insert into testTime values(?,?)',(d,t))
			print "date and time logged"
		except:
			print "Error"
			#exception thrown if database error
logTime()
