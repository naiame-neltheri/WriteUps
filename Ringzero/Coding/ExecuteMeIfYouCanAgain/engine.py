import sys
import requests
import subprocess
BASE_URL = "https://ringzer0ctf.com/challenges/125"
_COOKIE = "p6be62hl0v0eibhv66vrtldu52"

def get_task():
	print("[+] Getting task")
	r = requests.get(BASE_URL, cookies = {"PHPSESSID" : _COOKIE})
	raw = r.text
	if "----- BEGIN SHELLCODE -----" in raw:
		begin = raw.find("----- BEGIN SHELLCODE -----")+33
		end = raw.find("----- END SHELLCODE -----")-10
		print("[+] Task fetched successfully")
		return raw[begin:end].strip()
	else:
		print("[+] Something went wrong please check cookie")
		return False

def generate_payload(shellcode):
	print("[+] Generating payload")
	payload = '''
	#include <stdio.h>
	unsigned char code[] = "{}";
	int main(int argc, char **argv){{
		int foo_value = 0;
		int (*foo)() = (int(*)())code;
		foo_value = foo();
	}}
	'''.format(shellcode)
	print("[+] Payload generated successfully")
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
			return False
		else:
			return out.decode()

def send_flag(flag):
	r = requests.get(__BASE_URL + "/{}".format(flag), cookies = {"PHPSESSID" : _COOKIE})
	raw = r.text
	if "Wrong answer or too slow" in raw:
		print("[-] FLAG is wrong or too slow\n[-] Retrying")
		return True
	else:
		__regex = re.compile("FLAG-\w+")
		result = __regex.search(raw)
		print("[+] Flag is {}".format(result.group()))
		return False

if "__main__" in __name__:
	task = get_task()
	if task:
		payload = generate_payload(task)
		with open('tmp.c', 'w') as f:
			f.write(payload.strip())
		answer = execute_shell()
		if answer:
			send_flag(answer)
	else:
		sys.exit(1)