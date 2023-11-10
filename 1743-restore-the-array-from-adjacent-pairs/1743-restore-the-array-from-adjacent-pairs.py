class Solution:
    def restoreArray(self, Graph: List[List[int]]) -> List[int]:
        A = defaultdict(list)
        for a, b in Graph:
            A[a].append(b)
            A[b].append(a)
        res = [-1]
        for a in A:
            if len(A[a]) == 1:
                res[0], Q = a, [a]
                visit = {a}
        while Q:
            node = Q.pop(0)
            for child in A[node]:
                if child not in visit:
                    visit.add(child)
                    res.append(child)
                    Q.append(child)
        return res