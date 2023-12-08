class Solution:
    def closestCost(self, B: List[int], T: List[int], target: int) -> int:
        self.res, self.min_ = inf, inf
        @cache
        def dfs(i, key):
            if self.min_ > abs(key-target):
                self.min_ = abs(key-target)
                self.res = key
            elif self.min_ == abs(key-target):
                self.res = min(self.res, key)
            if i == len(T): 
                return
            dfs(i+1, key)
            dfs(i+1, key+T[i])
            dfs(i+1, key + T[i]*2)
            
        for c in B:
            dfs(0, c)
        return self.res 