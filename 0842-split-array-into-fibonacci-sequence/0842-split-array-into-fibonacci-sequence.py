class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res, self.ans = [], []
        def dfs(i):
            if i == len(num):
                if len(res) >= 3:
                    self.ans = res.copy()
                return
            for j in range(i, min(i+10, len(num))):
                if len(res) >= 2:
                    if int(num[i:j+1]) == res[-1]+res[-2] and num[i:j+1] == str(int(num[i: j+1])) and int(num[i:j+1]) < 2**31:
                        res.append(int(num[i:j+1]))
                        f = dfs(j+1)
                        res.pop()
                else:
                    if num[i:j+1]==str(int(num[i:j+1])):
                        res.append(int(num[i:j+1]))
                        f = dfs(j+1)
                        res.pop()
        dfs(0)
        return self.ans