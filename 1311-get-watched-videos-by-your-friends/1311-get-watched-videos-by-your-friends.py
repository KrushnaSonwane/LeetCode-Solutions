class Solution:
    def watchedVideosByFriends(self, W: List[List[str]], F: List[List[int]], id: int, level: int) -> List[str]:
        adj = defaultdict(list)
        for i, A in enumerate(F):
            for a in A:
                adj[i].append(a)
        visit, Q = set({id}), [id]
        for _ in range(level):
            for _ in range(len(Q)):
                node = Q.pop(0)
                for child in adj[node]:
                    if child not in visit:
                        visit.add(child)
                        Q.append(child)
        hashT, A = defaultdict(int), []
        for i in Q:
            for a in W[i]:
                hashT[a] += 1
        A = sorted([[hashT[ch], ch] for ch in hashT])
        return [a for _, a in A]