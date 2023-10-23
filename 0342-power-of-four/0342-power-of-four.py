class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        s = bin(num)[3:]
        return num!=0 and ('1' not in s) and len(s)%2 == 0