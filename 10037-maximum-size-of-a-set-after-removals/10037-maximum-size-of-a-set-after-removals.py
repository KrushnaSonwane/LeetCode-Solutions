class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = set(nums1), set(nums2)
        n = len(nums1)
        a, b = len(A), len(B)
        for num in A:
            if a > n // 2:
                if num in B:
                    B.discard(num)
                    a -= 1
            else:
                break
        for num in B:
            if b > n // 2:
                if num in A:
                    A.discard(num)
                    b -= 1
            else:
                break
        for num in B:
            A.add(num)
        res = len(A)
        if a >  n // 2:
            res -= (a - (n//2))
        if b > n // 2:
            res -= (b - (n // 2))
        return res