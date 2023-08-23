class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        A, visit = set(), set()
        i, j = 0, 9
        while len(s) > j:
            res = s[i:j+1]
            if res not in A: A.add(res)
            else: visit.add(res)
            j += 1
            i += 1
        return [ans for ans in visit]