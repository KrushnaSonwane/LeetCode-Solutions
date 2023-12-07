class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ''
        for i in range(len(num)):
          if num[i] in '13579':
            res = num[:i+1]
        return res