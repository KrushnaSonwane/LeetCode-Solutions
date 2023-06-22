class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0: return len(tasks)
        hashT = {}
        for ch in tasks:
            if ch not in hashT: hashT[ch] = 1
            else: hashT[ch] += 1
        queue = [ -hashT[val] for val in hashT]
        heapq.heapify(queue)
        res = 0
        while queue:
            curr = n + 1
            temp = []
            while queue and curr:
                temp.append(heapq.heappop(queue))
                curr -= 1
                res += 1
            res += curr
            while temp:
                val = temp.pop() + 1
                if val != 0: heapq.heappush(queue, val)
        return res - curr