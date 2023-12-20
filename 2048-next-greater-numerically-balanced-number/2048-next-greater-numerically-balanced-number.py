class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for num in range(n+1, 7777777):
            num = str(num)
            hashT = Counter(num)
            for a in hashT:
                if hashT[a] != int(a): 
                    break
            else:
                return int(num)
        return 1224444