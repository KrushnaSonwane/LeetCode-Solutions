class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res, max_ = [], -1
        for num in arr[::-1]:
            res.append(max_)
            max_ = max(max_, num)
        return res[::-1]