class Solution:
    def numOfBurgers(self, a: int, b: int) -> List[int]:
        if not a and not b: return [0, 0]
        l, r = 0, b
        while r > l:
            mid = (r + l) // 2
            if mid * 4 > a: r = mid
            else:
                t1, t2 = a - mid * 4, b - mid
                if t2 * 2 == t1: return [mid, t2]
                else:
                    if t2 * 2 > t1: r = mid
                    else: l = mid + 1
        return []