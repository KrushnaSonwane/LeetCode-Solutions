class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        res = []
        for i, a in enumerate(mat):
            b = a.copy()
            b = deque(b)
            for _ in range(k):
                if i % 2 == 0:
                    b.append(b.popleft())
                else:
                    b.appendleft(b.popleft())
            res.append(list(b))
        return res == mat