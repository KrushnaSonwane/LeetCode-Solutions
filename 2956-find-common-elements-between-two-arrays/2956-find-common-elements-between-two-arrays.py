class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = 0, 0
        for num in nums1:
            if nums2.count(num) >= 1:
                a += 1
        for num in nums2:
            if nums1.count(num) >= 1:
                b += 1
        return [a, b]