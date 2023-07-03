class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        color = defaultdict(str)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        for num in range(n):
            if num not in color:
                Q = [[num, 0]]
                while Q:
                    node, c = Q.pop(0)
                    color[node] = c
                    for child in adj[node]:
                        if child not in color:
                            Q.append([child, not c])
                            color[child] = not c
                        else:
                            if color[child] == c: return False
        return True