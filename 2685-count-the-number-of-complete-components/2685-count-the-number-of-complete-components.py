class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        res, visit = 0, set()
        for x in range(n):
            hashT = defaultdict(int)
            if x not in visit:
                totalNode = 1
                queue = [x]
                visit.add(x)
                while queue:
                    node = queue.pop(0)
                    for child in adj[node]:
                        hashT[node] += 1
                        if child not in visit:
                            visit.add(child)
                            queue.append(child)
                            totalNode += 1
                for val in hashT:
                    if hashT[val] != totalNode - 1:
                        break
                else:
                    res += 1
        return res