# Nest writeup
Scan ports using nmap and found 445, 4386 tcp ports.
4386 was unknown atm so I have used 445 to enumerate shares. And there was these shares
```
msf5 auxiliary(scanner/smb/smb_enumshares) > run

[+] 10.10.10.178:445      - ADMIN$ - (DISK) Remote Admin
[+] 10.10.10.178:445      - C$ - (DISK) Default share
[+] 10.10.10.178:445      - Data - (DISK) 
[+] 10.10.10.178:445      - IPC$ - (IPC) Remote IPC
[+] 10.10.10.178:445      - Secure$ - (DISK) 
[+] 10.10.10.178:445      - Users - (DISK) 
[*] 10.10.10.178:         - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```
xRxRxPANCAK3SxRxRx -> C.Smith
XtH4nkS4Pl4y1nGX -> Administrator
