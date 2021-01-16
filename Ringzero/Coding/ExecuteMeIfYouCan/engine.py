import re
import requests
import subprocess

__COOKIE = "s0sg59p7hme4rfg0tngnj69ui5"
__BASE_URL = "https://ringzer0ctf.com/challenges/121"

def get_data():
	r = requests.get(__BASE_URL, cookies = {"PHPSESSID" : __COOKIE})
	raw = r.text
	__start = raw.find("----- BEGIN SHELLCODE -----") + 33
	__end = raw.find("----- END SHELLCODE -----") - 10
	return raw[__start:__end].strip()

def generate_payload(shellcode):
	payload = '''
	#include <stdio.h>
	unsigned char code[] = "{}";
	int main(int argc, char **argv){{
		int foo_value = 0;
		int (*foo)() = (int(*)())code;
		foo_value = foo();
	}}
	'''.format(shellcode)
	return payload

def execute_shell():
	print("[+] Executing command 'gcc -fno-stack-protector -z execstack tmp.c -o tmp'")
	proc = subprocess.Popen("gcc -fno-stack-protector -z execstack tmp.c -o tmp", shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	out, err = proc.communicate()
	if err:
		print("[-] Error occured : {}".format(err))
	else:
		print("[+] Executing command ./tmp 0>&1")
		proc = subprocess.Popen("./tmp 0>&1", shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
		out, err = proc.communicate()
		if err:
			print("[+] OUTPUT : {}".format(out))
			print("[+] ERROR : {}".format(err))
		else:
			return out.decode()

def send_flag(flag):
	r = requests.get(__BASE_URL + "/{}".format(flag), cookies = {"PHPSESSID" : __COOKIE})
	raw = r.text
	if "Wrong answer or too slow" in raw:
		print("[-] FLAG {} is wrong or too slow\n[-] Retrying")
		return True
	else:
		__regex = re.compile("FLAG-\w+")
		result = __regex.search(raw)
		print("[+] Flag is {}".format(result.group()))
		return False

if "__main__" in __name__:
	state = True
	while state:
		print("[+] Fetching raw data")
		raw = get_data()
		print("[+] Generating C code")
		payload = generate_payload(raw)
		with open("tmp.c", "w") as f:
			f.write(payload)
		print("[+] Payload written to tmp.c")
		print("[+] Executing C code")
		flag = execute_shell()
		print("[+] Got flag {}\n[+] Sending flag waiting for result".format(flag))
		state = send_flag(flag)

# FLAG-W2gudjVCAlhexK1c3IfPun0CGs