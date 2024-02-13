class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        m, n = len(nums1), len(nums2)
        for i in range(m):
            j = 0
            while n > j:
                count = 0
                if nums1[i] == nums2[j]:
                    ptr = i
                    while m > ptr and j < n and nums1[ptr] == nums2[j]:
                        count += 1
                        ptr += 1
                        j += 1
                else:
                    j += 1
                res = max(res, count)
        for i in range(n):
            j = 0
            while m > j:
                count = 0
                if nums2[i] == nums1[j]:
                    ptr = i
                    while n > ptr and j < m and nums2[ptr] == nums1[j]:
                        count += 1
                        ptr += 1
                        j += 1
                else:
                    j += 1
                res = max(res, count)
        return res