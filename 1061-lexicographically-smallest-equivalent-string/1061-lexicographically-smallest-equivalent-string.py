class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)
        for a, b in zip(s1, s2):
            adj[a].append(b)
            adj[b].append(a)
        hashT = {}
        def dfs(i):
            visit = set({i})
            Q, min_ = [i], i
            while Q:
                node = Q.pop(0)
                min_ = min(min_, node)
                for child in adj[node]:
                    if child not in visit:
                        Q.append(child)
                        visit.add(child)
            return min_
        for i in range(97, 123):
            node = chr(i)
            hashT[node] = dfs(node)
        return ''.join([hashT[child] for child in baseStr])