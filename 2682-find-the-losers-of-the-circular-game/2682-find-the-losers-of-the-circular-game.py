class Solution(object):
    def circularGameLosers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        hashT = defaultdict(int)
        hashT[1] = 1
        currBoll = 1
        for i in range(1, n + 1):
            for _ in range(k * i):
                currBoll += 1
                if currBoll > n:
                    currBoll = 1
            hashT[currBoll] += 1
            if hashT[currBoll] == 2:
                break
        res = []
        for i in range(1, n + 1):
            if i not in hashT:
                res.append(i)
        return res