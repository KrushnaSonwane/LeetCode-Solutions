class Solution:
    def maximumRows(self, A: List[List[int]], numSelect: int) -> int:
        def isValid(li, masks):
            sum_ = numSelect - sum(1 for m in masks if m == '1')
            for j, num in enumerate(li):
                if num and masks[j] == '0':
                    sum_ -= 1
                    masks[j] = '1'
            return masks, sum_ >= 0

        @cache
        def dfs(i, mask):
            if i == len(A): return 0
            res = dfs(i+1, mask)
            B, valid = isValid(A[i], list(mask))
            if valid:
                res = max(res, dfs(i+1, ''.join(B)) + 1)
            return res
        return dfs(0, '0'*len(A[0]))