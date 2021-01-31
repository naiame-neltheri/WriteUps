# 7e9529962260edd36a2b2263a04131a621718e4b.
import hashlib, threading

_HASH = "7e9529962260edd36a2b2263a04131a621718e4b"

def gensha(key: str, salt: str):
	tmp_salt = hashlib.sha1(salt.encode('utf-8')).hexdigest()
	tmp_hash = hashlib.sha1(str(key + tmp_salt.lower()).encode('utf-8')).hexdigest()
	return tmp_hash

def breaker(start, end):
	for i in range(start, end):
		for t in range(start, end):
			print(f"[*] HASH : {_HASH} | KEY : {i} | SALT : {t}")
			# print(f"START : {start} END : {end}")
			if _HASH == gensha(str(i), str(t)):
				print(f"[+] Key found : {i}")
				break

if "__main__" in __name__:
	thread_count = 4
	threads = []
	divider = int((10000 - 1000) / 4)
	starts = []
	ends = []
	current = 1000
	for i in range(0, thread_count):
		starts.append(current)
		current += divider
		ends.append(current)
	try:
		for i in range(0, thread_count):
			t = threading.Thread(target = breaker, args = (starts[i], ends[i],), name = f"Thread ID {i}")
			threads.append(t)
			t.start()
	except Exception as error:
		print(f"[-] Error occured : {error}")

	except KeyboardInterrupt:
		print(f"[-] Killing {thread_count} threads")
		for t in threads:
			t.kill_received = True