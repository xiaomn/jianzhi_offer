# 题目描述(力扣)
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
# 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
# 简单分析
# 这道题很容易理解，也很简单，最简单的就是遍历，同时用一个哈希表去存储已经遍历过的元素，遍历的同时去哈希表查找词元素之前是否出现过。
# 但是面试题一般没有这么直接，肯定有其他的陷阱，能想到这一点，还是很不错的，接下来就看下面的揭发吧！

# -*- coding:utf-8 -*-

class Solution: 
    def findRepeatNumber(self, nums: List[int]) -> int:
		i = 0
		
		while i < len(nums):
			if nums[i] == i:
				i += 1
				continue
			if nums[i] == nums[nums[i]]:
				return nums[i]
			nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
		
		return -1

# 这道题可以这样思考，既然数组长度为 n ，而且存储的数字都在 0~n-1 之间，那么如果对于数组中的每个元素，i = nums[i] ，那么肯定有元素不满足，
# 那么这个元素就是重复的，所以我们要做的就是将nums中的元素进行互换，使其下标等于存储的元素。
        
        


