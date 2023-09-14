class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hashT = defaultdict(list)
        for a, b in tickets:
            hashT[a].append(b)
        for a in hashT:
            hashT[a].sort()
        res = []
        def dfs(root):
            while hashT[root]:
                dfs(hashT[root].pop(0))
            res.append(root)
        dfs('JFK')
        return res[::-1]