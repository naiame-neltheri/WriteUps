import requests
import hashlib
import time

BASE_URL = "https://ringzer0ctf.com/challenges/13"
M_COOKIE = dict(PHPSESSID="5ljcq42rd6bl01liavlp08mcf7")

def generate_data(): # Send request to base url extract the problem string
	r = requests.get(BASE_URL, cookies = M_COOKIE)
	raw = r.text
	start = raw.find("----- BEGIN MESSAGE -----") + 31
	end = raw.find("----- END MESSAGE -----") - 10
	content = raw[start:end].strip()
	return content

def send_result(data): # Send hash value to flag url print result html
	flag_url = BASE_URL + "/{}".format(data)
	r = requests.get(flag_url, cookies = M_COOKIE)
	raw = r.text
	print(raw)

def engine():
	time_start = time.time()
	data = generate_data()
	res = hashlib.sha512(data.encode('utf8')).hexdigest()
	time_end = time.time()
	if (time_end - time_start) < 2:
		send_result(res)
		return False
	else:
		print("[-] Too slow. Restarting...")
		return True

if '__main__' in __name__:
	state = True
	while(state):
		state = engine()

#FLAG-mukgu5g2w932t2kx1nqnhhlhy4