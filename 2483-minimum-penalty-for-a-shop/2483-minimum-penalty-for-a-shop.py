class Solution:
    def bestClosingTime(self, cust: str) -> int:
        count = cust.count("Y")
        res, min_ = 0, count
        for i, c in enumerate(cust):
            count += 1 if c == 'N' else -1
            if min_ > count:
                res, min_ = i+1, count
        return res