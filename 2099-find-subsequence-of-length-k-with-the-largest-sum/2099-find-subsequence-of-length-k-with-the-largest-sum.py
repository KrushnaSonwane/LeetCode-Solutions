class Solution:
    def maxSubsequence(self, A: List[int], k: int) -> List[int]:
        B, visit = sorted(A), defaultdict(int)
        for i in range(k):
            visit[B[len(A)-i-1]] += 1
        res = []
        for num in A:
            if visit[num]:
                visit[num] -= 1
                res.append(num)
        return res