class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        hashT = defaultdict(list)
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    hashT[i].append([abs(A[i][0]-A[j][0]) + abs(A[i][1]-A[j][1]), j])
        for i in hashT:
            hashT[i].sort()
        visit, res, Q = set({0}), 0, [0]
        while len(visit) != len(A):
            hq = []
            heapify(hq)
            for i in Q:
                while hashT[i] and hashT[i][0][1] in visit:
                    hashT[i].pop(0)
                if hashT[i]:
                    heappush(hq, [hashT[i][0][0], hashT[i][0][1]])
            sum_, j = heappop(hq)
            res += sum_
            visit.add(j)
            Q.append(j)
        return res