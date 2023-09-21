class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        for _ in range((m + n) // 2 - (1 if (m+n) % 2 == 0 else 0)):
            if m > i and n > j:
                if nums1[i] > nums2[j]:
                    j += 1
                else:
                    i += 1
            elif m > i:
                i += 1
            else:
                j += 1
        if (m+n) % 2:
            if m > i and n > j:
                return min(nums1[i], nums2[j]) / 1
            elif m > i:
                return nums1[i] / 1
            return nums2[j] / 1 
        sum_ = 0
        for _ in range(2):
            if m > i and n > j:
                if nums1[i] > nums2[j]:
                    sum_ += nums2[j]
                    j += 1
                else:
                    sum_ += nums1[i]
                    i += 1
            elif m > i:
                sum_ += nums1[i]
                i += 1
            else:
                sum_ += nums2[j]
                j += 1
        return sum_ / 2.00