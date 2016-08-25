sys.path.append(os.path.join(os.path.dirname(__file__), "requests"))
import sys, os
import requests 


# needleInHaystack: iterates through the strings in hayStackList, and if needle is equal to a string in the list
# return index at which needle is found
def needleInHaystack ():
	r = requests.post("http://challenge.code2040.org/api/haystack", data={'token': '747bece10e7785955b91c15de7435216'})
	result = r.json()
	hayStackList = result["haystack"]
	needle = result["needle"]
	for i in range(0, len(hayStackList)):
		if hayStackList[i] == needle:
			r2 = requests.post("http://challenge.code2040.org/api/haystack/validate", data={'token': '747bece10e7785955b91c15de7435216', 'needle': i})
	return -1 # needle not found in hayStack 

needleInHaystack()