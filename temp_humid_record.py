import sqlite3
import sys
import Adafruit_DHT

def log_values(sensorID,temp,humid):
	conn=sqlite3.connect("/var/www/lab_app/lab_app.db")
	
	cursor=conn.cursor()
	cursor.execute("""Insert into temperature values(datetime('now'),(?),(?))""",(sensorID,temperature))
	cursor.execute("""Insert into humidity values(datetime('now'),(?),(?))""",(sensorID,humidity))
	conn.commit()		
	conn.close()

humidity,temperature=Adafruit_DHT.read_retry(11,4)

if humidity is not None and temperature is not None:
	log_values("1",temperature,humidity)
else:

	log_values("1",0,0)
	
