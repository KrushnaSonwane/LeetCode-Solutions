import bisect
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.hashT = defaultdict(list)
        for i, num in enumerate(arr): self.hashT[num].append(i)

    def query(self, l: int, r: int, val: int) -> int:
        return bisect_right(self.hashT[val], r) - bisect_left(self.hashT[val], l)

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)