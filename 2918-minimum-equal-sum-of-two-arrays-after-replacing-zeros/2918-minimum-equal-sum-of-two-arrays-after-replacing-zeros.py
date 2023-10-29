class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = nums1.count(0)
        b = nums2.count(0)
        aa, bb = sum(nums1), sum(nums2)
        if a == 0 and aa < b + bb: return -1
        if b == 0 and bb < aa + a: return -1
        return max(aa + a, bb + b)