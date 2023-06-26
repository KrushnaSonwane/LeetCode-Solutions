class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        if not d: return []
        hashT = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        res = []
        def dfs(i, s):
            if i == len(d):
                res.append(''.join(s))
                return
            s.append('')
            for ch in hashT[d[i]]:
                s[i] = ch
                dfs(i + 1, s)
        dfs(0, [])
        return res