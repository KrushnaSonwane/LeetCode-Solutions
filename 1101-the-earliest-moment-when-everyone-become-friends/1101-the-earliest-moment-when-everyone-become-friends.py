class Solution:
    def earliestAcq(self, A: List[List[int]], n: int) -> int:

        def check(k):
            adj = defaultdict(list)
            for i in range(k+1):
                c, a, b = A[i]
                adj[a].append(b)
                adj[b].append(a)
            Q, visit = [0], set({0})
            while Q:
                node = Q.pop(0)
                for child in adj[node]:
                    if child not in visit:
                        visit.add(child)
                        Q.append(child)
            return len(visit) == n

        A.sort()
        res = -1
        l, r = 0, len(A)-1
        while r >= l:
            mid = (r + l) // 2
            if check(mid):
                res = A[mid][0]
                r = mid - 1
            else:
                l = mid + 1
        return res