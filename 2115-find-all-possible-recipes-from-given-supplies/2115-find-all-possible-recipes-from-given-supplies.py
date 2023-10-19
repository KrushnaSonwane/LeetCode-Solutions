class Solution:
    def findAllRecipes(self, R: List[str], I: List[List[str]], S: List[str]) -> List[str]:
        S, res = set(S), []
        for _ in range(len(R)):
            for i, food in enumerate(R):
                if food in S: continue
                count = 0
                for ing in I[i]:
                    if ing not in S:
                        count += 1
                if count == 0:
                    res.append(food)
                    S.add(food)
        return res