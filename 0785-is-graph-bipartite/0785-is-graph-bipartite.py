class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        adj = defaultdict(list)
        for i in range(n):
            for node in graph[i]:
                adj[i].append(node)
        colors, visit = [-1] * n, set()
        for i in range(n):
            if i not in visit:
                visit.add(i)
                queue, colors[i] = [[i, 1, 2]], 1
                while queue:
                    node, curr, prev = queue.pop(0)
                    for child in adj[node]:
                        if colors[child] == curr: return False
                        colors[child] = prev
                        if child not in visit:
                            visit.add(child)
                            queue.append([child, prev, curr])
        return True
