class Solution:
    def countMatches(self, items: List[List[str]], key: str, val: str) -> int:
        res = 0
        for ty, clr, nme in items:
            res += (key == 'type' and val == ty) or (key == 'color' and val == clr) or (key == 'name' and val == nme)
        return res