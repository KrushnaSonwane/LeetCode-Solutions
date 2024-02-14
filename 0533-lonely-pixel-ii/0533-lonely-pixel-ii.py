class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m, n = len(picture), len(picture[0])
        freq = defaultdict(int)
        rows = [0] * m
        cols = [0] * n
        for i in range(m): 
            for j in range(n): 
                if picture[i][j] == "B": 
                    rows[i] += 1
                    cols[j] += 1
            freq["".join(picture[i])] += 1
        
        ans = 0
        for i in range(m):
            key = "".join(picture[i])
            if freq[key] == target: 
                for j in range(n): 
                    if picture[i][j] == "B" and rows[i] == cols[j] == target: ans += 1
        return ans 