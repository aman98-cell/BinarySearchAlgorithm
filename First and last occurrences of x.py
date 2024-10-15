# User function Template for python3
class Solution:
    def firstAndLast(self, x, arr):

        # Code here
        def first(arr, x):
            n = len(arr)
            left = 0
            right = n - 1
            fi = -1
            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == x:
                    fi = mid
                    right = mid - 1
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return fi

        def second(arr, x):
            n = len(arr)
            left = 0
            right = n - 1
            sec = -1
            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == x:
                    sec = mid
                    left = mid + 1
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return sec

        findex = first(arr, x)
        sindex = second(arr, x)

        if findex == -1 or sindex == -1:
            return [-1]
        else:
            return [findex, sindex]


arr = [1, 3, 3, 4]
x  = 3
instance = Solution()
print(instance.firstAndLast(x,arr))


