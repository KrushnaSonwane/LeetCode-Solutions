class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        W = set(words)
        def dfs(i, size):
            if (i, size) not in dp:
                if i == len(w):
                    return size == 2
                res = False
                for j in range(i, len(w)):
                    if w[i: j+1] in W:
                        res = res or dfs(j+1, min(size+1, 2))
                dp[(i, size)] = res
            return dp[(i, size)]
        
        res = []
        for w in W:
            dp = {}
            if dfs(0, 0):
                res.append(w)
        return res