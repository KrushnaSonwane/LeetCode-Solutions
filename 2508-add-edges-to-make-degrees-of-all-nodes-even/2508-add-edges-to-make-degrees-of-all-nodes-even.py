class Solution(object):
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        degree = defaultdict(list)
        for u, v in edges:
            degree[u].append(v)
            degree[v].append(u)
        edges = {(u, v) for u, v in edges}
        odd = []
        for node in degree:
            if len(degree[node]) % 2:
                odd.append(node)
        m = len(odd)
        if not m: return 1
        if m > 4 or m % 2: return 0
        if m == 2:
            if (odd[0], odd[1]) not in edges and (odd[1], odd[0]) not in edges: return 1
            for i in range(1, n + 1):
                if i != odd[0] and i != odd[1]:
                    if (i, odd[0]) not in edges and (odd[0], i) not in edges and (i, odd[1]) not in edges and (odd[1], i) not in edges: return 1
            return False
        for i in range(m):
            for j in range(m):
                if i == j: continue
                for k in range(m):
                    if k == i or k == j: continue
                    for l in range(m):
                        if l in [i, j, k]: continue
                        if (odd[i], odd[j]) not in edges and (odd[j], odd[i]) not in edges:
                            if (odd[k], odd[l]) not in edges and (odd[l], odd[k]) not in edges:
                                return 1
        return 0
