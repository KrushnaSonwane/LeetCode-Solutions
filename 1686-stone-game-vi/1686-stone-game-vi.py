class Solution:
    def stoneGameVI(self, alice: List[int], bob: List[int]) -> int:
        A = sorted([[a+b, i] for i, (a, b) in enumerate(zip(alice, bob))])
        sum_, count = 0, True
        for _, i in A[::-1]:
            sum_ += alice[i] if count else -bob[i]
            count = not count
        if sum_ > 0: return 1
        elif sum_ < 0: return -1
        else: return 0