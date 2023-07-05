class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        def dfs(num):
            nonlocal res
            if num > high: return
            if low <= num and high >= num: res.append(num)
            if str(num)[-1] == '9': return
            num = str(num) + str(int(str(num)[-1]) + 1)
            dfs(int(num))
        for i in range(1, 9): dfs(i)
        return sorted(res)