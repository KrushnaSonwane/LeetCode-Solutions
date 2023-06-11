class Solution:
    def minSwaps(self, s: str) -> int:
        res = [ch for ch in s]
        l, r = 0, len(res) - 1
        ans = 0
        left, right = 0, 0
        while r > l:
            while left >= 0 and r > l:
                left += 1 if res[l] == '[' else -1
                l += 1
            if left < 0:
                l -= 1
            while right >= 0 and r > l:
                right += 1 if res[r] == ']' else -1
                r -= 1
            if right < 0:
                r += 1
            if left == right == -1:
                res[l], res[r] = res[r], res[l]
                ans += 1
            if res[l] != ']': left = 0
            if res[r] != '[': right = 0
        return ans