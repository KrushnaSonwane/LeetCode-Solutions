class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        adj = defaultdict(list)
        for a, b in pairs:
            adj[a].append(b)
            adj[b].append(a)
        s = [s[i] for i in range(len(s))]
        visit = set()
        for i in range(len(s)):
            if i not in visit:
                visit.add(i)
                index, ch, Q = [i], [s[i]], [i]
                while Q:
                    node = Q.pop(0)
                    for child in adj[node]:
                        if child not in visit:
                            index.append(child)
                            ch.append(s[child])
                            visit.add(child)
                            Q.append(child)
                ch.sort()
                index.sort()
                for c in ch:
                    s[index.pop(0)] = c
        return ''.join(s)