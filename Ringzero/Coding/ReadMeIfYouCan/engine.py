try:
	from PIL import Image, ImageOps, ImageEnhance
except ImportError:
	import Image, ImageOps, ImageEnhance

import re
import numpy as np
import requests, base64
import pytesseract, cv2
from io import BytesIO
from bs4 import BeautifulSoup

__COOKIE = "5b29rf082r9kr66q9n167cvad5"
BASE_URL = "https://ringzer0ctf.com/challenges/17"

def get_image():
	r = requests.get(BASE_URL, cookies = {"PHPSESSID" : __COOKIE})
	soup = BeautifulSoup(r.content, "html.parser")
	resp = soup.find_all('img')
	return resp[1]['src']

def read_image(img_str):
	img_str = img_str.split('base64,')[-1].strip()
	img_string = BytesIO(base64.b64decode(img_str))
	img = Image.open(img_string)
	img.save('orig.png')
	img = img.convert('L')
	img.save('gray.png')

	pixels = img.load()
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			if pixels[i,j] != 255:
				pixels[i,j] = 0

	img.save('mine.png')
	invert = ImageOps.invert(img)
	invert.save('invert.png')

	# BELOW SECTION WILL CHANGE ONLY TEXT COLOR
	# data = np.array(img)
	# red, green, blue, alpha= data.T

	# white_areas = (red == 255) & (blue == 255) & (green == 255)
	# data[..., :-1][white_areas.T] = (0, 0 , 0)
	# res = Image.fromarray(data)
	# res.save('convtest.png')

	# invert = ImageEnhance.Contrast(invert)
	# invert = invert.enhance(3)

	data = pytesseract.image_to_string(invert)
	# data = ""
	print("[+] RESULT : {}".format(data))
	return data.strip()

def send_flag(flag):
	r = requests.get(BASE_URL + "/{}".format(flag), cookies = {"PHPSESSID" : __COOKIE})
	raw = r.text
	if "Wrong answer or too slow" in raw:
		print("[-] FLAG is wrong or too slow\n[-] Retrying")
		return True
	else:
		__regex = re.compile("FLAG-\w+")
		result = __regex.search(raw)
		print("[+] Flag is {}".format(result.group()))
		return False

if "__main__" in __name__:
	state = True
	while state:
		print("[+] Fetching base64 image")
		b64_image = get_image()
		print("[+] Processing base64 image")
		text = read_image(b64_image)
		print("[+] Image read successfullly : {}".format(text))
		print("[+] Sending answer")
		state = send_flag(text)
