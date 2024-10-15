from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
nums = [-1,0,3,5,9,12]
target = 9

instance = Solution()
print(instance.search(nums,9))