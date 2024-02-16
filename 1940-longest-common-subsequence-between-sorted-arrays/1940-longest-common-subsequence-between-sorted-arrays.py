class Solution:
    def longestCommonSubsequence(self, A: List[List[int]]) -> List[int]:
        max_, hashT = 0, Counter()
        for a in A:
            for num in a:
                hashT[num] += 1
                max_ = max(max_, num)
        res = []
        for i in range(1, max_+1):
            if hashT[i] == len(A):
                res.append(i)
        return res