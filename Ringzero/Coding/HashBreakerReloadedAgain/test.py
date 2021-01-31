import string, time, hashlib, random

TIME_LIMIT = 2.5
_HASH = "7e9529962260edd36a2b2263a04131a621718e4b"

def breaker():
	key = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
	tmp_hash = hashlib.sha1(key.encode()).hexdigest()
	print(f"[*] Trying key : {key}")
	if tmp_hash == _HASH:
		print(f"[+] Key found : {key}")
		return False
	return True

	# start = time.time()
	# for string in itertools.product(POOL, repeat = WIDTH): 
	# 	tmp_hash = hashlib.sha1("".join(string).encode('utf-8')).hexdigest()
	# 	print(f"[*] Trying key : {''.join(string)}")
	# 	if _HASH == tmp_hash:
	# 		print(f"[+] Key found : {''.join(string)}")

if "__main__" in __name__:
	is_searching = True
	while is_searching:
		is_searching = breaker()