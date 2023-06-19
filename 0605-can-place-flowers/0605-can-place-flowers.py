class Solution(object):
    def canPlaceFlowers(self, flow, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        res = 0
        for val in flow:
            if val == 0: count += 1
            else:
                if res == 0:
                    n -= count // 2
                else:
                    if count >= 2:
                        if count % 2 == 0:
                            count -= 1
                    n -= count // 2
                count = 0
                res += 1
        if res == 0:
            if count % 2 == 0: n -= count // 2
            else:
                n -= (count // 2) + 1
        else:
            n -= count // 2
        return 0 >= n