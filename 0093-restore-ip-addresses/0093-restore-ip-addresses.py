class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, nums = [], []
        def dfs(i):
            if i == len(s):
                if len(nums)==4:
                    res.append('.'.join(nums))
                return
            for j in range(i, min(len(s), i+3)):
                if 0 <= int(s[i:j+1]) <= 255 and str(int(s[i:j+1]))==s[i:j+1]:
                    nums.append(s[i:j+1])
                    dfs(j+1)
                    nums.pop()
        dfs(0)
        return res