import requests

BASE_URL = "https://ringzer0ctf.com/challenges/125"
_COOKIE = {"PHPSESSID" : "obibui0cvng75r2l1b25cln2n2"}

def get_shellcode():
	r = requests.get(BASE_URL, cookies = _COOKIE)
	resp = r.text
	begin = resp.find("----- BEGIN SHELLCODE -----") + 33
	end = resp.find("----- END SHELLCODE -----") - 10
	shellcode = resp[begin:end].strip()
	print(shellcode)

if "__main__" in __name__:
	get_shellcode()