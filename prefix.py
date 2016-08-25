import sys, os, json
sys.path.append(os.path.join(os.path.dirname(__file__), "requests"))
import requests 

def findNonPrefixes(prefix, array):
	result = []
	prefixLength = len(prefix)
	for string in array:
		if string[0:prefixLength] != prefix: 
			result.append(string)
	return result

def run ():
	r = requests.post("http://challenge.code2040.org/api/prefix", data={'token': '747bece10e7785955b91c15de7435216'})
	result = r.json()
	prefix = result["prefix"]
	stringArray = result["array"]
	resultArray = findNonPrefixes(prefix, stringArray)
	headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
	payload = {'token': '747bece10e7785955b91c15de7435216', 'array': resultArray}
	r2 = requests.post("http://challenge.code2040.org/api/prefix/validate", data=json.dumps(payload), headers = headers)
run()