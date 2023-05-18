class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set({word for word in bank})
        visit = set({start})
        queue, allCh = [start], 'ACGT'
        res = 0
        while queue:
            for _ in range(len(queue)):
                curr = list(queue.pop(0))
                if curr == list(end): return res
                for i in range(8):
                    back = curr[i]
                    for ch in allCh:
                        if curr[i] == ch: continue
                        curr[i] = ch
                        temp = ''.join(curr)
                        if temp not in visit and temp in bank:
                            visit.add(temp)
                            queue.append(temp)
                        curr[i] = back
            res += 1
        return -1