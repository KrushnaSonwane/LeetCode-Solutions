class Solution:
    def minimumHammingDistance(self, S: List[int], T: List[int], A: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in A:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        res = 0
        for num in range(len(S)):
            if num not in visit:
                Q = [num]
                visit.add(num)
                curr = [num]
                while Q:
                    node = Q.pop(0)
                    for child in adj[node]:
                        if child not in visit:
                            Q.append(child)
                            curr.append(child)
                            visit.add(child)
                count = defaultdict(int)
                for i in curr:
                    count[S[i]] += 1
                for i in curr:
                    if count[T[i]]:
                        count[T[i]] -= 1
                        res += 1
        return len(S)-res