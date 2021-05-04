def checkArr(nums):
	for i in range(0,len(nums)):
		if i + 1 > len(nums) - 1:
			break
		if nums[i + 1] < nums[i]:
			return i + 1
	return -1

def solve(nums):
	_max, is_modified = nums[0], False
	state = checkArr(nums)
	if state == 0:
		nums[state] = nums[1] - 1
	elif state == -1:
		return True
	elif state == 1:
		nums[0] = nums[state]
	else:
		if state != len(nums) - 1:
			if nums[state] < nums[state + 1] and nums[state - 1] > nums[state] and nums[state - 1] < nums[state + 1]:
				nums[state] = nums[state - 1]
			else:
				nums[state - 1] = nums[state]
		else:
			nums[state] = nums[state - 1]
	print(nums)
	state = checkArr(nums)
	if state == -1:
		return True
	else:
		return False

if "__main__" in __name__:
	# print(solve([4,2,1]), "4,2,1")
	# print(solve([1,1,1]), "1,1,1")
	# print(solve([3,2,1,4]), "3,2,1,4")
	# print(solve([3,4,2,3]), "3,4,2,3")
	# print(solve([4,2,3]), "4,2,3")
	# print(solve([-1,4,2,3]), "-1,4,2,3")
	# print(solve([5,7,1,8]), "5,7,1,8")
	print(solve([-1,4,2,3]), "-1,4,2,3")