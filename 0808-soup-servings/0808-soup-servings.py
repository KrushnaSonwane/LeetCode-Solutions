class Solution:
    def soupServings(self, N: int) -> float:
        if N > 4800: return 1
        @cache
        def f(a, b):
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            return 0.25 * (f(a - 4, b) + f(a - 3, b - 1) + f(a - 2, b - 2) + f(a - 1, b - 3))
        N = math.ceil(N / 25.0)
        return f(N, N)