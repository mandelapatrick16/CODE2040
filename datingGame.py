sys.path.append(os.path.join(os.path.dirname(__file__), "requests"))
import sys, os, json
import requests 
import dateutil.parser
import datetime 

# addInterval: takes a date and an interval (interger which specifies number of seconds)
# return newDate with interval added 
def addInterval(date, interval):
	oldTime = dateutil.parser.parse(date)
	newTime = oldTime + datetime.timedelta(seconds=interval)
	newTimeString = str(newTime.isoformat())
	return newTimeString.replace("+00:00","Z") # python gives UTC isoformat as +00:00 however, API accepts Z


def run ():
	r = requests.post("http://challenge.code2040.org/api/dating", data={'token': '747bece10e7785955b91c15de7435216'})
	result = r.json()
	datestamp = result["datestamp"]
	interval = result["interval"]
	newTimeStamp = addInterval(datestamp, interval)
	r2 = requests.post("http://challenge.code2040.org/api/dating/validate", data={'token': '747bece10e7785955b91c15de7435216', 'datestamp': newTimeStamp})
	print (r2.status_code, r2.reason)
run()