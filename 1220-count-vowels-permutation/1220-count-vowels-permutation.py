class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9+7
        hashT = {' ': 'aeiou', 'a': 'e', 'e': 'ia', 'i': 'aeou', 'o': 'iu', 'u': 'a'}
        @cache
        def dfs(i, last):
            if i == n: return 1
            res = 0
            for ch in hashT[last]:
                res += dfs(i+1, ch)
            res %= MOD
            return res
        return dfs(0, ' ')