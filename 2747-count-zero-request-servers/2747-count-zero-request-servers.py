class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x: (x[1]))
        Q = [[val, i] for i, val in enumerate(queries)]
        Q.sort()
        res = [0] * len(Q)
        count, ptr1, ptr2 = 0, 0, 0
        hashT = defaultdict(int)
        for key, i in Q:
            while len(logs) > ptr2 and logs[ptr2][1] <= key:
                hashT[logs[ptr2][0]] += 1
                count += hashT[logs[ptr2][0]] == 1
                ptr2 += 1
            while len(logs) > ptr1 and key - x > logs[ptr1][1]:
                hashT[logs[ptr1][0]] -= 1
                count -= hashT[logs[ptr1][0]] == 0
                ptr1 += 1
            res[i] = n - count
        return res