class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, nums = [], []
        def dfs(i):
            if len(nums) > 4: return
            if i == len(s):
                if len(nums)==4:
                    for num in nums:
                        if 0 <= int(num) <= 255 and str(int(num)) == num: continue
                        else: return
                    else:
                        res.append('.'.join(nums))
                return
            for j in range(i, len(s)):
                nums.append(s[i: j+1])
                dfs(j+1)
                nums.pop()
        dfs(0)
        return res