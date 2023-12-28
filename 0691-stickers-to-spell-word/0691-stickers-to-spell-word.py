class Solution:
    def minStickers(self, s: List[str], t: str) -> int:
        @cache
        def dfs(i, mask):
            if '0' not in mask: return 0
            if i == len(s):
                return 0 if '0' not in mask else inf
            res = dfs(i+1, mask)
            A = [ch for ch in mask]
            size = 1
            flag = True
            while flag:
                chnage = False
                for _, ch in enumerate(s[i]):
                    if ch not in t: continue
                    for j in range(len(A)):
                        if A[j] == '0' and t[j] == ch:
                            A[j] = '1'
                            chnage = True
                            break
                flag = chnage
                res = min(res, dfs(i+1, ''.join(A.copy())) + size)
                size += 1
            return res
        res = dfs(0, '0'*len(t))
        return -1 if res == inf else res