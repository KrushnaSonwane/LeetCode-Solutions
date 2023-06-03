class Solution:
    def memLeak(self, m1: int, m2: int) -> List[int]:
        curr = 1
        flag = True
        while True:
            if m2 > m1:
                if curr <= m2: m2 -= curr
                else: break
            else:
                if curr <= m1: m1 -= curr
                else: break
            curr += 1
        return [curr, m1, m2]