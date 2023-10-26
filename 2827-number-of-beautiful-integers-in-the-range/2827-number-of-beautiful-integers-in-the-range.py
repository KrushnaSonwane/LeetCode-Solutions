class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        @cache
        def dfs(s, index, odd, even, remainder, tight, leadingZero):
            if index >= len(s):
                return remainder % k == 0 and odd == even
            
            bound = int(s[index]) if tight else 9
            ans = 0
            for digit in range(bound + 1):
                add_odd = digit % 2 == 1
                add_even = digit % 2 == 0
                
                if leadingZero and digit == 0:
                    add_even = 0
                    
                ans += dfs(s, index + 1,
                           odd + add_odd,
                           even + add_even,
                           (remainder*10 + digit) % k,
                           tight and digit == int(s[index]),
                           leadingZero and digit == 0)
            return ans
        
        return dfs(str(high), 0, 0, 0, 0, True, True) - dfs(str(low - 1), 0, 0, 0, 0, True, True)