# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, obj: 'MountainArray') -> int:
        l, r = 0, obj.length()-1
        mid = -1
        
        while r >= l:
            m = (r+l) // 2
            if m == 0:
                l = 1
            elif m == obj.length()-1:
                r = m - 1
            else:
                a, b, c = obj.get(m-1), obj.get(m), obj.get(m+1)
                if a < b > c:
                    mid = m
                    break
                elif a < b:
                    l = m + 1
                else:
                    r = m - 1
                
        l, r = 0, mid
        
        while r >= l:
            m = (r + l) // 2
            ele = obj.get(m)
            if ele == target:
                return m
            elif ele > target:
                r = m - 1
            else:
                l = m + 1
                
        l, r = mid, obj.length()-1
        
        while r >= l:
            m = (r+l) // 2
            ele = obj.get(m)
            if ele == target:
                return m
            elif ele > target:
                l = m + 1
            else:
                r = m - 1
                
        return -1