class Solution:
    def relocateMarbles(self, nums: List[int], A: List[int], B: List[int]) -> List[int]:
        hashT = collections.defaultdict(int)
        for num in nums:
            hashT[num] += 1
        for a, b in zip(A, B):
            if a in hashT:
                count = hashT[a]
                del hashT[a]
                hashT[b] += count
        res = []
        for num in hashT:
            res.append(num)
        return sorted(res)