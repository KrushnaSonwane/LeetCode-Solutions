class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        adj = defaultdict(list)
        for i in range(1, n):
            adj[i].append(i+1)
            adj[i+1].append(i)
        adj[x].append(y)
        adj[y].append(x)
        res = [0 for _ in range(n)]
        for i in range(1,n+1):
            count, Q, visit = 0, [i], set({i})
            while Q:
                for _ in range(len(Q)):
                    node = Q.pop(0)
                    for child in adj[node]:
                        if child not in visit:
                            visit.add(child)
                            Q.append(child)
                res[count] += len(Q)
                count += 1
            
        return res