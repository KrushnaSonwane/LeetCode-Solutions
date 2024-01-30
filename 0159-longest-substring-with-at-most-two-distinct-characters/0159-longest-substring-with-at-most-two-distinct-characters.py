class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res, j, hashT = 0, 0, Counter()
        for i, ch in enumerate(s):
            hashT[ch] += 1
            while len(hashT) == 3:
                hashT[s[j]] -= 1
                if hashT[s[j]] == 0: del hashT[s[j]]
                j += 1
            res = max(res, i - j + 1)
        return res