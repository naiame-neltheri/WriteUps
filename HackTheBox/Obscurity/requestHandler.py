import socket
import json

HOST = '10.10.10.168'
PORT = 8080

try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
		sc.connect((HOST, PORT))
		print("[+] Connected to host {} : {}".format(HOST, PORT))
		print("[+] Sending data through socket")
		data = {
			"method" : "get",
			"doc" : "/etc/issue",
			"header" : "Content-Type: application/json\nAccept: application/json",
			"vers" : '1.0',
			"body" : "test"
		}
		sc.sendall(json.dumps(data).encode('utf8'))
		resp = sc.recv(1024)
		print(resp.decode())
except Exception as e:
	print("[-] Unhandled exception occured : {}".format(e))