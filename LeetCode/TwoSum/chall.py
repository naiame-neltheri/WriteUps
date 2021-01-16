import itertools

# SLOW
class Solution():

	def twoSum(self, nums, target):
		resp = []
		for a, b in itertools.combinations(enumerate(nums), 2):
			index_a, value_a = a
			index_b, value_b = b
			if (value_a + value_b) == target:
				resp.append(index_a)
				resp.append(index_b)
		return resp

# FAST
class Solution2():

	def twoSum(self, nums: list, target: int):
		prevMap = {}
		for i, n in enumerate(nums):
			diff = target - n
			if diff in prevMap:
				return [prevMap[diff], i]
			prevMap[n] = i

if "__main__" in __name__:
	obj = Solution2()
	res = obj.twoSum([3,2,4], 6)
	print(res)