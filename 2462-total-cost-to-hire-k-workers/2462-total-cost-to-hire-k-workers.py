class Solution(object):
    def totalCost(self, costs, k, emp):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        A, B = [], []
        l, r = 0, len(costs) - 1
        for _ in range(emp):
            heappush(A, [costs[l], l])
            l += 1
        for _ in range(emp):
            if l <= r:
                heappush(B, [costs[r], r])
                r -= 1
            else: break
        res = 0
        while k:
            a, i = heappop(A) if A else [float("inf"), 0]
            b, j = heappop(B) if B else [float("inf"), 0]
            if a > b:
                res += b
                if r >= l:
                    heappush(B, [costs[r], r])
                    r -= 1
                if a != float("inf"): heappush(A, [a, i])
            else:
                res += a
                if r >= l:
                    heappush(A, [costs[l], l])
                    l += 1
                if b != float("inf"): heappush(B, [b, j])
            k -= 1
        return res