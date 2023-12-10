class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        s = 'abcdefghijklmnopqrstuvwxyz'
        @cache
        def dfs(i, last):
            if i == len(word): return 0
            res = inf
            if word[i] != last and abs(ord(word[i]) - ord(last)) != 1:
                res = dfs(i+1, word[i])
            for ch in s:
                if ch == last: continue
                if abs(ord(ch) - ord(last)) == 1: continue
                res = min(res, dfs(i+1, ch) + 1)
            return res
        res = inf
        for ch in s:
            res = min(res, dfs(0, ch))
        return res