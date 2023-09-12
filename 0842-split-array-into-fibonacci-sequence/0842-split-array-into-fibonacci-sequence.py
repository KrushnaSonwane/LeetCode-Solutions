class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res, self.ans = [], []
        max_ = 2**31
        def dfs(i):
            if i == len(num):
                if len(res) >= 3:
                    self.ans = res.copy()
                return
            for j in range(i, min(i+10, len(num))):
                a, aa = int(num[i:j+1]), num[i:j+1]
                if len(res) >= 2:
                    if a == res[-1]+res[-2] and a < max_ and aa == str(a):
                        res.append(a)
                        dfs(j+1)
                        res.pop()
                else:
                    if a < max_ and aa == str(a):
                        res.append(a)
                        dfs(j+1)
                        res.pop()
        dfs(0)
        return self.ans