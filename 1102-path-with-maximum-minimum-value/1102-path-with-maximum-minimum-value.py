class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:

        def isValid(k):
            if A[0][0] < k: return False
            Q, visit = [[0, 0]], set({(0, 0)})
            while Q:
                i, j = Q.pop(0)
                if (i, j) == (len(A)-1, len(A[0])-1): return True
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= x < len(A) and 0 <= y < len(A[0]) and (x, y) not in visit and A[x][y] >= k:
                        Q.append([x, y])
                        visit.add((x, y))
            return False

        l, r = 0, 10**9
        res = 0
        while r >= l:
            mid = (r + l) // 2
            if isValid(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res