# 1. Check SMB
If there is SMB there is shared disk or something so check with showmount -e 10.10.10.180 will result site_backups
# 2. Search for something
Mount found share and search for something. And found administrator hash
`adminadmin@htb.localb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}admin@htb.localen-USfeb1a998-d3bf-406a-b30b-e269d7abdf50`
# 3. Crack with john
`john hash --format=Raw-SHA1 --wordlist=<WORDLIST>`
