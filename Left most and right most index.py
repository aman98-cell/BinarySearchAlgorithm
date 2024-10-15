class Solution:
    def index(self, arr, target):
        # Helper function to find the first index of the target
        def firstIndex(arr, target):
            n = len(arr)
            left = 0
            right = n - 1
            first = -1  # Initialize with -1, meaning not found
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    first = mid  # Record the index and continue searching to the left
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        # Helper function to find the last index of the target
        def lastIndex(arr, target):
            n = len(arr)
            left = 0
            right = n - 1
            last = -1  # Initialize with -1, meaning not found
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    last = mid  # Record the index and continue searching to the right
                    left = mid + 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        # Find the first and last index of the target
        first_index = firstIndex(arr, target)
        last_index = lastIndex(arr, target)

        return (first_index, last_index)


# Example usage:
arr = [1, 3, 5, 5, 5, 5, 7, 123, 125]
target = 7
instance = Solution()
print(instance.index(arr, target))
