import requests
import base64

BASE_URL = "https://ringzer0ctf.com/challenges/16"
_COOKIE = {"PHPSESSID" : "obibui0cvng75r2l1b25cln2n2"}

def get_task():
	req = requests.get(BASE_URL, cookies = _COOKIE)
	resp = req.text
	key_start = resp.find("----- BEGIN XOR KEY -----") + 31
	key_end = resp.find("----- END XOR KEY -----") - 10
	key = resp[key_start:key_end].strip()
	cipher_start = resp.find("----- BEGIN CRYPTED MESSAGE -----") + 39
	cipher_end = resp.find("----- END CRYPTED MESSAGE -----") - 10
	cipher = resp[cipher_start:cipher_end].strip()
	print(f"[+] KEY : {key}\n[+] CIPHER : {cipher}")
	return {"key" : key, "cipher" : cipher}

def decrypt_msg(obj):
	cipher = base64.b64decode(obj["cipher"])
	print(type(cipher))
	for _char in cipher:
		print(_char)
	keyByte = 0
	for _char in obj['key']:
		keyByte += ord(_char)
		print(ord(_char))
	print(keyByte)

if "__main__" in __name__:
	print("[+] STARTING")
	obj = get_task()
	decrypt_msg(obj)