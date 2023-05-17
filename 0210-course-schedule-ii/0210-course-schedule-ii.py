class Solution(object):
    def findOrder(self, n, graph):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degree, adj, visit = [0] * n, defaultdict(list), set()
        for a, b in graph:
            adj[b].append(a)
            degree[a] += 1
        queue, res = [], []
        for i, val in enumerate(degree):
            if not val:
                res.append(i)
                queue.append(i)
                visit.add(i)
        while queue:
            node = queue.pop(0)
            for child in adj[node]:
                degree[child] -= 1
                if degree[child] == 0 and child not in visit:
                    queue.append(child)
                    visit.add(child)
                    res.append(child)
        return res if len(res) == n else []