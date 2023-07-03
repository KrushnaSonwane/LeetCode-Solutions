class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = [ch for ch in s]
        n, sum_ = len(s), 0
        for i in range(n-1, -1, -1):
            sum_ += shifts[i]
            curr = ((ord(s[i]) - 97) + sum_) % 26
            res[i] = chr(curr + 97)
        return ''.join(res)