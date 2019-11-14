import requests

BASE_URL = "https://ringzer0ctf.com/challenges/32"
SESSION_ID = "nlqji6vu9gik51op373jbt7ob0"

def generate_data():
	r = requests.get(BASE_URL, cookies = {"PHPSESSID" : SESSION_ID})
	if r.status_code != 200:
		print("[-] Request failed status code : {}".format(r.status_code))
		return False
	raw = r.text
	if "(Do not brute force / hack this one)" in raw:
			print("[-] Login required !!!")
			return False
	start = raw.find("----- BEGIN MESSAGE -----") + 31
	end = raw.find("----- END MESSAGE -----") - 10
	return raw[start:end].strip()

def calculate_math(content):
	content = content.split(" ")
	res = int(content[0], 10) + int(content[2], 16) - int(content[4], 2)
	return res

def send_flag(solution):
	solUrl = BASE_URL + "/{}".format(solution)
	r = requests.get(solUrl, cookies = {"PHPSESSID" : SESSION_ID})
	print("[+] Sending request to {}".format(solUrl))
	if r.status_code != 200:
		print("[-] Request failed status code : {}".format(r.status_code))
	raw = r.text
	if "(Do not brute force / hack this one)" in raw:
			print("[-] Login required !!!")
			return False
	if "FLAG" in raw:
		start = raw.find("FLAG")
		print(raw[start:start+100])
		print("FOUND FLAG")
		return True
	elif "Wrong" in raw:
		print("[-] Wrong or too slow")
		return False

def engine():
	print("[+] Generating data...")
	content = generate_data()
	if not content:
		return False
	print("[+] Calculating math...")
	res = calculate_math(content)
	print("[+] Requesting flag...")
	if send_flag(res):
		return True
	else:
		return False

if "__main__" in __name__:
	is_running = True
	while is_running:
		if engine():
			is_running = False