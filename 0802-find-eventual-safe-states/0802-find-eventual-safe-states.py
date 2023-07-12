class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        path, visit = [0] * n, [0] * n
        adj = defaultdict(list)
        for i in range(n):
            for node in graph[i]:
                adj[i].append(node)
        
        def cycle(node):
            if visit[node] and path[node]: return True
            if visit[node]: return False
            visit[node] = 1
            path[node] = 1
            for child in adj[node]:
                if cycle(child):
                    return True
            path[node] = 0
            return False

        for i in range(n):
            if not visit[i]:
                cycle(i)
        return [i for i in range(n) if not path[i]]