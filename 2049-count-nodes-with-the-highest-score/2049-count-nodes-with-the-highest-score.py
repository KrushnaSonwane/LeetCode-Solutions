class Solution(object):
    def countHighestScoreNodes(self, parents):
        adj, n = defaultdict(list), len(parents)
        for i, par in enumerate(parents):
            adj[par].append(i)
        hashT = defaultdict(int)
        children = defaultdict(list)
        def dfs(node, parent):
            sum_ = 0
            for child in adj[node]:
                sum_ += 1 + dfs(child, node)
            hashT[node] = sum_
            children[parent].append(node)
            return sum_
        dfs(0, -1)
        res, max_ = 0, 0
        for node in hashT:
            prod = 1
            nodes = 0
            for child in children[node]:
                prod = prod * (hashT[child] + 1)
                nodes += hashT[child] + 1
            prod = prod * max(1, n - nodes - 1)
            if prod > max_:
                max_ = prod
                res = 0
            res += prod == max_
        return res