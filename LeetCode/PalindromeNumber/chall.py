class Solution():

	def isPalindrome(self, x):
		if x > 0:
			backward = str(x)[::-1]
			if int(x) == int(backward):
				return True
			else:
				return False
		return False

if "__main__" in __name__:
	obj = Solution()
	res = obj.isPalindrome(121)
	print(f"[+] Result : {res}")