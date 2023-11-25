from sortedcontainers import SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], Q: List[List[int]]) -> List[int]:
        res = [inf for _ in Q]
        Q = sorted([[size, pref, i] for i, (pref, size) in enumerate(Q)])[::-1]
        R = sorted([[size, id] for i, (id, size) in enumerate(rooms)])[::-1]
        A = SortedList()
        for size, key, i in Q:
            while R and R[0][0] >= size:
                sz, id = R.pop(0)
                A.add(id)
            ans = bisect_right(A, key-1)
            min_ = inf
            if ans < len(A):
                res[i] = A[ans]
                min_ = abs(A[ans]-key)
            if ans-1 >= 0:
                diff = abs(A[ans-1]-key)
                if min_ > diff:
                    res[i] = A[ans-1]
                elif min_ == diff:
                    res[i] = min(res[i], A[ans-1])
            if res[i] == inf: res[i] = -1
        return res