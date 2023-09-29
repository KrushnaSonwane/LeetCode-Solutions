class Solution:
    def removeSubfolders(self, A: List[str]) -> List[str]:
        A = sorted([[len(a), a] for a in A])
        res, hashT = [], set()
        for _, a in A:
            i = 0
            while _ > i:
                while _ > i and a[i] != '/':
                    i += 1
                if a[:i] in hashT:
                    break
                i += 1
            else:
                res.append(a)
            hashT.add(a)
        return res