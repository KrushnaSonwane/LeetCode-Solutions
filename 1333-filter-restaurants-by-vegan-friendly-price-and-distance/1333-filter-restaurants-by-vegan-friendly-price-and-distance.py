class Solution:
    def filterRestaurants(self, R: List[List[int]], F: int, P: int, D: int) -> List[int]:
        R.sort(key = lambda x : (-x[1], -x[0]))
        res = []
        for ids, rate, frd, price, dist in R:
            if ((F and frd) or not F) and price <= P and dist <= D:
                res.append(ids)
        return res