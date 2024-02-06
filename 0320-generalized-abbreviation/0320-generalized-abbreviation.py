class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        def dfs(i, s):
            if i >= len(word):
                res.append(s)
                return
            dfs(i+1, s + word[i])
            for j in range(i, len(word)):
                t = s
                t += str(j-i+1) + ('' if j+1 >= len(word) else word[j+1])
                dfs(j+2, t)
        dfs(0, '')
        return res