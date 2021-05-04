# Script Kiddie notes
- Identifying web service was one of the hardest one on this box
- After the identification, the CVE [2020-7384](https://cvedetails.com/cve/CVE-2020-7384/)
- The previous exploit will result reverse shell with user KID -> PWN
- The root was easy. msfconsole could be ran as root using sudo without password, thus after msfconsole /bin/bash will
  invoke root privileged shell
