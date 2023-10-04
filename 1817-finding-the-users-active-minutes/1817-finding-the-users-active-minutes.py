class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashT = defaultdict(set)
        for id, time in logs:
            hashT[id].add(time)
        res = [0 for _ in range(k)]
        for id in hashT:
            res[len(hashT[id])-1] += 1
        return res