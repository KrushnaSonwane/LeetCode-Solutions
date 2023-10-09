class Solution:
    def searchRange(self, A: List[int], key: int) -> List[int]:
        def getLeft():
            l, r = 0, len(A) - 1
            res = -1
            while r >= l:
                m = (l + r) // 2
                if A[m] == key:
                    res = m
                    r = m - 1
                elif A[m] > key:
                    r = m - 1
                else:
                    l = m + 1
            return res
        def getRight():
            l, r = 0, len(A) - 1
            res = -1
            while r >= l:
                m = (l + r) // 2
                if A[m] == key:
                    res = m
                    l = m + 1
                elif A[m] > key:
                    r = m - 1
                else:
                    l = m + 1
            return res
        return [getLeft(), getRight()]