import requests
import time
import hashlib, binascii

BASE_URL = "https://ringzer0ctf.com/challenges/14"
SESS_ID = "nlqji6vu9gik51op373jbt7ob0"

def generate_data():
	r = requests.get(BASE_URL, cookies = {"PHPSESSID" : SESS_ID})
	if r.status_code != 200:
		return "ERROR - STATUS {}".format(r.status_code)
	raw = r.text
	if "----- BEGIN MESSAGE -----" not in raw:
		return "LOGIN FAILED"
	start = raw.find("----- BEGIN MESSAGE -----") + 31
	end = raw.find("----- END MESSAGE -----") - 10
	return raw[start:end].strip()

def get_flag(solution):
	print("[+] Sending request to : {}".format(BASE_URL + "/{}".format(str(solution))))
	r = requests.get(BASE_URL + "/{}".format(str(solution)), cookies = {"PHPSESSID" : SESS_ID})
	if r.status_code != 200:
		print("[-] Status code wrong")
		return False
	raw = r.text
	if "FLAG" in raw:
		flag = raw.find("FLAG")
		print(raw[flag: flag+100])
		print("FLAG FOUND")
		return True
	elif "Wrong answer or too slow!" in raw:
		print("[-] Wrong answer or too slow!")
		return False
	elif "(Do not brute force / hack this one)" in raw:
		print("[-] Login required !!!")
		return True

def convert2ascii(content):
	res = ''
	n = 8
	tmp = [(content[i:i+n]) for i in range(0, len(content), n)]
	for item in tmp:
		res += chr(int(item, 2))
	return res

def engine():
	start = time.time()
	print("[+] Generating data...")
	content = generate_data()
	if "LOGIN FAILED" in content:
		print("[-] Login required !!!")
		return True
	print("[+] Generating hash...")
	content = convert2ascii(content)
	res = hashlib.sha512(content.encode('utf8')).hexdigest()
	end = time.time()
	if (end - start) > 2:
		print("[-] Operation took {}... Restarting".format(end - start))
		return False
	print("[+] Sending hash...")
	if not get_flag(res):
		return False
	else:
		return True

if "__main__" in __name__:
	is_running = True
	while is_running:
		if not engine():
			is_running = True
		else:
			is_running = False