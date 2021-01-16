from struct import pack, error

class Solution():

# FIRST TRY
	# def reverse(self, x):
	# 	is_signed = False
	# 	raw = str(x)[::-1]
	# 	if "-" in raw:
	# 		raw = raw.replace("-", "")
	# 		is_signed = True
	# 	print(len(bin(int(raw))))
	# 	if len(bin(int(raw))) - 1 <= 32:
	# 		return -int(raw) if is_signed else int(raw)
	# 	else:
	# 		return 0

# UPDATED SPEED
	def reverse(self, x):
		is_signed = False
		if x <= 2147483648:
			raw = str(x)[::-1]
			if "-" in raw:
				raw = raw.replace("-", "")
				is_signed = True
			if len(bin(int(raw))) - 1 <= 32:
				return -int(raw) if is_signed else int(raw)
			else:
				return 0
		else:
			return 0

if "__main__" in __name__:
	obj = Solution()
	res = obj.reverse(-2147483412)
	print(f"[+] Result : {res}")