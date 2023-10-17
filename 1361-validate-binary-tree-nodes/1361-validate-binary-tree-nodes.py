class Solution:
    def validateBinaryTreeNodes(self, n: int, LL: List[int], RR: List[int]) -> bool:
        allNode = set()
        for i, (a, b) in enumerate(zip(LL, RR)):
            for x in [a, b]:
                if x != -1:
                    allNode.add(x)
        Q = []
        for i in range(n):
            if i not in allNode:
                Q.append(i)
                allNode.add(i)
        if len(Q) != 1: return False
        visit = set({Q[0]})
        while Q:
            node = Q.pop(0)
            for child in [LL[node], RR[node]]:
                if child == -1: continue
                if child in visit: return False
                Q.append(child)
                visit.add(child)
        return len(visit) == len(allNode) == n