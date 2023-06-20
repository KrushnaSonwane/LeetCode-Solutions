class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans, res = 0, []
        n = len(seats)
        for i, ch in enumerate(seats):
            if ch: res.append(i)
        ans = res[0]
        for i in range(len(res)):
            if i == len(res) - 1: ans = max(ans, n - res[i] - 1)
            dist = res[i] - res[i - 1]
            ans = max(ans, dist // 2)
        return ans