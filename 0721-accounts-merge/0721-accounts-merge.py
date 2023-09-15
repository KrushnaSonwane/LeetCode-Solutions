class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hashT = defaultdict(list)
        for i, A in enumerate(accounts):
            for a in A[1:]:
                hashT[a].append(i)
        adj = defaultdict(list)
        for e in hashT:
            for i in hashT[e]:
                for j in hashT[e]:
                    adj[i].append(j)
        visit, res = set(), []

        for i in adj:
            if i not in visit:
                Q = [i]
                t = set()
                while Q:
                    node = Q.pop(0)
                    for j in adj[node]:
                        if j not in visit:
                            visit.add(j)
                            Q.append(j)
                            for e in accounts[j][1:]:
                                t.add(e)
                t = [accounts[i][0]] + list(sorted(t))
                res.append(t)
        return res