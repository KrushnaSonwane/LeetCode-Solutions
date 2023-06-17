class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.hashT = defaultdict(list)
        for i, num in enumerate(arr):
            self.hashT[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if not self.hashT[value]: return 0
        l = bisect.bisect_left(self.hashT[value], left)
        r = bisect.bisect_right(self.hashT[value], right)
        return r - l

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)