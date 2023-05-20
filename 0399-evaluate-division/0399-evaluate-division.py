class Solution(object):
    def calcEquation(self, equations, values, queries):
        adj = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])
        res = []
        for a, b in queries:
            if a not in adj or b not in adj: 
                res.append(-1.00000)
                continue
            queue = [[a, 1.00000]]
            visit = {a}
            while queue:
                node, val = queue.pop(0)
                if node == b: 
                    res.append(val)
                    break
                for child, c in adj[node]:
                    if child not in visit:
                        visit.add(child)
                        queue.append([child, val * c])
            else:
                res.append(-1.00000)
        return res