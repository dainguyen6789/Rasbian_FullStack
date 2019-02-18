
from flask import Flask,request, render_template

app=Flask(__name__)

@app.route("/")
def hello():
	return "Hello Dai Nguyen, from Flask and Python 3"



@app.route("/temp")
def temp():
	import sys
	import Adafruit_DHT
	humidity,temperature=Adafruit_DHT.read_retry(11,4)
	if humidity is not None and temperature is not None:
		return render_template("lab_temp.html",temp=temperature,hum=humidity)
	else:
		return render_template("no_sensor.html")

if __name__=="__main__":
		app.run(host='0.0.0.0',port=8080)

