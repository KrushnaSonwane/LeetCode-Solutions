class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.hashT = Counter(nums2)
        self.nums2 = nums2
        self.nums1 = nums1

    def add(self, index: int, val: int) -> None:
        self.hashT[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.hashT[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.hashT[tot - num] for num in self.nums1)


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)