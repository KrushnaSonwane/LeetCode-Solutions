class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        hashT = defaultdict(list)
        for a, b in tickets:
            hashT[a].append(b)
        for a in hashT:
            hashT[a].sort()
        def dfs(start):
            while hashT[start]:
                dfs(hashT[start].pop(0))
            res.append(start)
        res = []
        dfs("JFK")
        return res[::-1]