class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        neg = False
        if 0 > num:
            neg = True
            num = -num
        res = 0
        arr = []
        while num:
            arr.append(num % 10)
            num //= 10
        arr.sort()
        if neg:
            for n in arr[::-1]:
                res *=10
                res += n
            return -res
        zero = arr.count(0)
        flag = False
        for n in arr:
            if not n: continue
            else:
                if not flag:
                    res = n
                    flag = True
                    if not zero: 
                        continue
                    res = res * pow(10, zero)
                else:
                    res *= 10
                    res += n
        return res
        