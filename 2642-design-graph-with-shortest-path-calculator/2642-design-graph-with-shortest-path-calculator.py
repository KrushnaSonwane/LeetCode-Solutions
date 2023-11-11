class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.A = defaultdict(list)
        self.dist = {}
        for a, b, w in edges:
            self.A[a].append([b, w])
        
    def addEdge(self, edge: List[int]) -> None:
        a, b, w = edge
        self.A[a].append([b, w])

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2: return 0
        Q, dist = [[0, node1]], {}
        heapify(Q)
        while Q:
            cost, node = heappop(Q)
            if node == node2:
                return cost
            for child, w in self.A[node]:
                if (node1, child) in dist and dist[(node1, child)] <= cost + w: continue
                dist[(node1, child)] = cost + w
                heappush(Q, [cost + w, child])      
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)