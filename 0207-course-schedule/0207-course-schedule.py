class Solution(object):
    def canFinish(self, n, graph):
        adj, visit, degree = defaultdict(list), set(), [0] * n
        for a, b in graph:
            adj[b].append(a)
            degree[a] += 1
        queue = []
        for i, val in enumerate(degree):
            if not val: 
                queue.append(i)
                visit.add(i)
        while queue:
            node = queue.pop(0)
            for child in adj[node]:
                degree[child] -= 1
                if degree[child] == 0 and child not in visit:
                    queue.append(child)
                    visit.add(child)
        return len(visit) == n