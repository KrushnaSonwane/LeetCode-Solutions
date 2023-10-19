#User function Template for python3
from collections import deque 
class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        q=deque()
        q.append((0,0))
        
        visited=set()
        visited.add(0)
        
        level=0
        
        while q:
            node,level=q.popleft()
            if node==X:
                return level
                
            for j in adj[node]:
                if j not  in visited:
                    visited.add(j)
                    q.append((j,level+1))
                    
        
            
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends