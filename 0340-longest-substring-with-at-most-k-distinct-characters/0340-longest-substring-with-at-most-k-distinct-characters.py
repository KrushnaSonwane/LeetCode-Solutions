class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashT = defaultdict(int)
        i, j = 0, 0
        res = 0
        while i < len(s):
            hashT[s[i]] += 1
            while len(hashT) > k:
                hashT[s[j]] -= 1
                if hashT[s[j]] == 0:
                    del hashT[s[j]]
                j += 1
            res = max(res, i - j + 1)
            i += 1
        return res