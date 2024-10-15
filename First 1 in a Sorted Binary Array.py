class Solution:
    def firstIndex(self, arr):
        # Your code goes here
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:

            mid = (left + right) // 2

            if mid == 0 and arr[mid] == 1:
                return 0

            if arr[mid] < 1:
                left = mid + 1
            elif arr[mid - 1] == 1:
                right = mid - 1
            else:
                return mid
        return -1

arr = [0,1,1]
instance = Solution()
print(instance.firstIndex(arr))