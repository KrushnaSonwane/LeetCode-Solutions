class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        res = -1
        for i, W in enumerate(strs):
            for j, T in enumerate(strs):
                if i == j: continue
                a = 0
                for ch in T:
                    if a < len(W):
                        a += W[a] == ch
                if a == len(W): break
            else:
                res = max(res, len(W))
        return res