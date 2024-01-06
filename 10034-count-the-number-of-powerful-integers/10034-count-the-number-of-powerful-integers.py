class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def solve(i, j, ss, tt, pre, A, dp):
            if (i, j, ss, tt, pre, A) not in dp:
                if j == len(s) and i == len(A):
                    return 1
                if i == len(A):
                    return 1 if j == len(s) else 0
                
                if ss:
                    res = 0
                    for num in range(0, limit+1):
                        if tt and num > int(A[i]): break
                        if not pre:
                            
                            res += solve(i+1, 0, 1, tt and str(num) == A[i], 0, A,dp)
                            if str(num) == s[j]:
                                res += solve(i+1, j+1, 1, tt and str(num) ==A[i], 1, A, dp)
                            
                        else:
                            if j < len(s):
                                if str(num) == s[j]:
                                    res += solve(i+1, j+1, 1, tt and str(num) == A[i], 1, A, dp)
                            
                            
                else:
                    res = solve(i+1, 0, 0, 0, 0, A, dp)
                    for num in range(1, limit+1):
                        if i == 0 and num > int(A[0]): break
                        res += solve(i+1, 0, 1, i == 0 and A[i] == str(num), 0, A, dp)
                        if str(num) == s[0]:
                            res += solve(i+1, 1, 1, i == 0 and A[i] == str(num), 1, A, dp)
                    
                dp[(i, j, ss, tt, pre, A)]  = res
                
            return dp[(i, j, ss, tt, pre, A)]
        res = solve(0, 0, 0, True, 0, str(finish), {}) - solve(0, 0, 0, True, 0, str(start-1), {})
        return res