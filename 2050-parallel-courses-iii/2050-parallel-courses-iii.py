class Solution(object):
    def minimumTime(self, n, relations, time):
        adj = defaultdict(list)
        visit, degree = set(), [0] * (n + 1)
        for a, b in relations:
            degree[b] += 1
            adj[a].append(b)
        hashT = defaultdict(int)
        queue = []
        for i in range(1, n + 1):
            if not degree[i]:
                visit.add(i)
                queue.append([i, time[i - 1]])
                hashT[i] = time[i - 1]
        res = 0
        while queue:
            node, t = queue.pop(0)
            res = max(res, t)
            for child in adj[node]:
                degree[child] -= 1
                hashT[child] = max(hashT[child], t)
                if child not in visit and degree[child] == 0:
                    queue.append([child, hashT[child] + time[child - 1]])
                    visit.add(child)
        return res