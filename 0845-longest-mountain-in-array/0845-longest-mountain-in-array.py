class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res, ptr, n = 0, 1, len(arr)
        while n > ptr:
            if arr[ptr] <= arr[ptr - 1]:
                ptr += 1
            else:
                left = ptr - 1
                while n > ptr and arr[ptr - 1] < arr[ptr]:
                    ptr += 1
                while n > ptr and arr[ptr - 1] > arr[ptr]:
                    ptr += 1
                    res = max(res, ptr - left)
        return res if res >= 3 else 0