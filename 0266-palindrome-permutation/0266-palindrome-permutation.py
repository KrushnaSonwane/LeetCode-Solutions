class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        A, count = Counter(s), 0
        for ch in A:
            count += A[ch] % 2
        return 2 > count