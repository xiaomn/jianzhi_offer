# 统计一个数字在排序数组中出现的次数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2 
# 
#  示例 2: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  
# 
#  注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
# position-of-element-in-sorted-array/ 
#  Related Topics 数组 二分查找 👍 249 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # method one
        # left = bisect.bisect_left(nums, target)
        # right = bisect.bisect_right(nums, target, lo=left)
        # return right - left

        # method two
        # return nums.count(target)

        # method three
        def search_left(nums: List[int], target: int) -> int:
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        def search_right(nums: List[int], target: int) -> int:
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        left = search_left(nums, target)
        if left == -1:
            return 0
        right = search_right(nums, target)
        return right - left + 1

# leetcode submit region end(Prohibit modification and deletion)
