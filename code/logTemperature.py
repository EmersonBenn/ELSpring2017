import os
import time
import sqlite3 as mydb
import sys
""" Log Current Time, Temperature in Celsius and Fahrenheit To an Sqlite3 database """
def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-00044a3df7ff/w1_slave") #opens temp sensor's data file
	tempfile_text = tempfile.read() #read in temp data
	currentTime=time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000 #format data
	tempF=tempC*9.0/5.0+32.0 #convert to F
	return [currentTime, tempC, tempF]


def logTemp():
	con = mydb.connect('temperatureLog.db')
	with con:
		try:
			[t,C,F]=readTemp()
			print "Current temperature is: %s F" %F
			cur = con.cursor()
			#sql = "insert into TempData values(?,?,?)"
			cur.execute('insert into TempData values(?,?,?)', (t,C,F)) #write temp log to database
			print "Temperature logged"
		except:
			print "Error!!"
			#exception thrown if error with database

#log temperature every 30 seconds 20 times
for i in range(0, 20):
	logTemp()
	time.sleep(30)
