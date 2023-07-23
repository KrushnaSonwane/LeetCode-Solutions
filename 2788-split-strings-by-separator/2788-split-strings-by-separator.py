class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            newS = word.replace(separator, ' ')
            newS = newS.split()
            for ch in newS:
                res.append(ch)
        return res