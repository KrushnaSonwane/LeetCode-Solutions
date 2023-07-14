class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        hashT = defaultdict(int)
        for a in arr:
            hashT[a] = hashT[a-d] + 1
        return max(hashT.values())