class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for _, b in paths:
            for a, _ in paths:
                if a == b: 
                    break
            else: 
                return b
        return b