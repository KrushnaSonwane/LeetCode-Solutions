class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        res = ''
        while r >= l:
            mid = (r + l) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                res = letters[mid] if not res else min(res, letters[mid])
                r = mid - 1
        return letters[0] if not res else res