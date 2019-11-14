import requests
import hashlib

BASE_URL = "http://docker.hackthebox.eu:41926/"
SESS = requests.Session()

def generate_quest():
	r = SESS.get(BASE_URL)
	if r.cookies.get_dict():
		tmp = r.cookies.get_dict()
		print(tmp)
		SESS.cookies.update(tmp)
	raw = r.text
	start = raw.find("<h3 align='center'>") + 19
	end = raw.find("</h3>")
	content = raw[start:end]
	return content

def send_solution(answer):
	m_data = {"hash":answer}
	m_proxy = {"http" : "http://127.0.0.1:8080", "https" : "http://127.0.0.1:8080"}
	r = SESS.post(BASE_URL, data = m_data, proxies = m_proxy)
	if r.cookies.get_dict():
		tmp = r.cookies.get_dict()
		SESS.cookies.update(tmp)
	raw = r.text
	print(raw)
	r = SESS.get(BASE_URL, proxies = m_proxy)
	raw = r.text
	return raw

if "__main__" in __name__:
	quest = generate_quest()
	m_hash = hashlib.md5(quest.encode('utf8')).hexdigest()
	flag = send_solution(m_hash)
	print(flag)