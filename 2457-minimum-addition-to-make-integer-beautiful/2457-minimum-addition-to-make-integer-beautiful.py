from collections import deque
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        queue, num = deque(), n
        while num:
            queue.appendleft(num % 10)
            num //= 10
        if sum(queue) < target: return 0
        def setQueue(i):
            while i >= 0:
                if queue[i] == 9:
                    queue[i] = 0
                else:
                    queue[i] += 1
                    break
                i -= 1
            return i
        temp = queue.copy()
        ptr = len(queue) - 1
        res = 0; currPower = 0
        while ptr >= 0 and sum(queue) > target:
            if queue[ptr] != 0:
                queue[ptr] = 9
                ptr = setQueue(ptr)
            else:
                ptr -= 1
        if sum(queue) == 0:
            sum_ = 1
            for _ in queue: sum_ *= 10
        else: 
            sum_ = ''
            for num in queue:
                sum_ = str(num) + sum_
            sum_ = sum_[::-1]
        sum2 = ''
        for num in temp:
            sum2 = str(num) + sum2
        return int(sum_) - int(sum2[::-1])