from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        left = 0
        right = n-1

        while left<=right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        if target > nums[mid]:
            return mid + 1
        else:
            return mid


nums = [1, 3, 5, 6]
target = 7
instance = Solution()
print(instance.searchInsert(nums,target))