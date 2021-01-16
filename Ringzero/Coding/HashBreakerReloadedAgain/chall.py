import requests
import random
import hashlib

SESS_ID = "vqe125prumq9nkuvl3bc1b65k4"


def generate_hash():
	r = requests.get('https://ringzer0ctf.com/challenges/159', cookies = {"PHPSESSID":SESS_ID})
	raw = r.text
	start = raw.find("----- BEGIN HASH -----") + 28
	end = raw.find("----- END HASH -----") - 10
	return raw[start:end].strip()

def breaker(_hash, tmp_answer):
	salt = hashlib.sha1(str(random.randint(1000,9999)).encode('utf8')).hexdigest()
	toHash = tmp_answer + salt
	tmpHash = hashlib.sha1(toHash.encode('utf8')).hexdigest()
	print("\r[*] TEMP Hash : {} vs {}".format(tmpHash, _hash), end="")
	if _hash == tmpHash:
		print("\n")
		print("[+] Found : {}".format(tmp_answer))
		return False
	else:
		return True

if "__main__" in __name__:
	_hash = generate_hash()
	is_running = True
	while is_running:
		is_running = breaker(_hash, str(random.randint(1000,9999)))