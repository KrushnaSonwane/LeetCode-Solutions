class Solution:
    def threeSumSmaller(self, A: List[int], target: int) -> int:
        A.sort()
        res = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                key = target - (A[i]+A[j])
                l, r = j+1, len(A)-1
                k = j
                while r >= l:
                    mid = (r + l) // 2
                    if A[mid] >= key:
                        r = mid - 1
                    else:
                        l = mid + 1
                        k = mid
                res += k - j
        return res