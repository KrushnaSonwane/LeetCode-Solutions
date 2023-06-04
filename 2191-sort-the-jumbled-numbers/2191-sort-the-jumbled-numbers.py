class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        hashT = defaultdict(list)
        for i, num in enumerate(nums):
            num = [ch for ch in str(num)]
            for j, digit in enumerate(num):
                num[j] = str(mapping[int(digit)])
            hashT[int(''.join(num))].append(i)
        return [nums[i] for num in sorted(hashT.keys()) for i in hashT[num]]