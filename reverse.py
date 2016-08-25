sys.path.append(os.path.join(os.path.dirname(__file__), "requests"))
import sys, os
import requests 

# had to convert to list to do modfications to string in python 
def reverse(string):
	if len(string) == 0 or len (string) == 1:
		return string

	start = 0
	end = len(string) - 1

	stringList = list(string)
	while start < end:
		temp = stringList[start]
		stringList[start] = stringList[end]
		stringList[end] = temp
		start += 1
		end -= 1

	return ''.join(stringList)

def run ():
	r = requests.post("http://challenge.code2040.org/api/reverse", data={'token': '747bece10e7785955b91c15de7435216'})
	reversedString = reverse(r.text)
	r2 = requests.post("http://challenge.code2040.org/api/reverse/validate", data={'token': '747bece10e7785955b91c15de7435216', 'string': reversedString})

run()
