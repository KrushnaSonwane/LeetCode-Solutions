class Solution:
    def goodDaysToRobBank(self, A: List[int], time: int) -> List[int]:
        res = []
        if time == 0: return [i for i in range(len(A))]
        l, r = 0, 0
        for i in range(1, min(time, len(A))):
            if A[i-1] <= A[i]: r += 1
            else: r = 0
        for i in range(1, len(A)):
            if A[i-1] >= A[i]: l += 1
            else: l = 0
            if i + time < len(A):
                if A[i+time-1] <= A[i+time]: r += 1
                else: r = 0
                if r >= time and l >= time:
                    res.append(i)
        return res