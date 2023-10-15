class Solution:
    def minimumDistance(self, word: str) -> int:
        hashT = {
        'A': [0,0], 'B': [0,1], 'C': [0,2], 'D': [0,3], 'E': [0,4], 'F': [0,5],
        'G': [1,0], 'H': [1,1], 'I': [1,2], 'J': [1,3], 'K': [1,4], 'L': [1,5],
        'M': [2,0], 'N': [2,1], 'O': [2,2], 'P': [2,3], 'Q': [2,4], 'R': [2,5],
        'S': [3,0], 'T': [3,1], 'U': [3,2], 'V': [3,3], 'W': [3,4], 'X': [3,5],
        'Y': [4,0], 'Z': [4,1]
        }
        def getDist(a, b):
            sum_ = 0
            for aa, bb in zip(hashT[a], hashT[b]):
                sum_ += abs(aa-bb)
            return sum_

        @cache
        def dfs(i, f, s):
            if i == len(word): 
                return 0
            if not f:
                res = dfs(i+1, word[i], s)
            else:
                res = dfs(i+1, word[i], s) + getDist(f, word[i])
            if not s:
                res = min(res, dfs(i+1, f, word[i]))
            else:
                res = min(res, dfs(i+1, f, word[i]) + getDist(s, word[i]))
            return res
        return dfs(0, '', '')