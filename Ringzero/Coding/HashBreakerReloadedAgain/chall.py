from random import randint
import hashlib, requests, threading

SESS_ID = "erhl8371egtjg3verliemh4st3"


def generate_hash():
	r = requests.get('https://ringzer0ctf.com/challenges/159', cookies = {"PHPSESSID":SESS_ID})
	raw = r.text
	start = raw.find("----- BEGIN HASH -----") + 28
	end = raw.find("----- END HASH -----") - 10
	return raw[start:end].strip()

def breaker(key):
	tmp_salt = hashlib.sha256(str(randint(1000,9999)).encode('utf-8')).hexdigest().lower()
	tmp_hash = hashlib.sha256((key + tmp_salt).encode('utf-8')).hexdigest().lower()
	return tmp_hash

def engine(_hash):
	is_searching = True
	while is_searching:
		key = str(randint(1000, 9999))
		print(f"[*] Brute forcing hash {_hash.lower()}. Trying key : {key} [THREAD-ID : {threading.current_thread().getName()}]")
		if _hash.lower() == breaker(key):
			print(f"[+] Found key : {key}")
			break

if "__main__" in __name__:
	thread_count = 4
	threads = []
	try:
		_hash = generate_hash()
		for i in range(0, thread_count):
			t = threading.Thread(target = engine, args = (_hash,), name = f"Thread-{i}")
			threads.append(t)
			t.start()
	except Exception as error:
		print(f"[-] Error occured : {error}")