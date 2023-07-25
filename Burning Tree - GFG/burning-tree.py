#User function Template for python3

class Solution:
    def minTime(self, root,target):
        self.rootMap = {root: None}
        self.arr = []
        def dfs(root):
            if not root: return
            if root.left: self.rootMap[root.left] = root
            if root.right: self.rootMap[root.right] = root
            if root.data == target: self.arr.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        # print(self.arr)
        res = 0
        if not self.arr: return res
        visited = set()
        res = -1
        while self.arr:
            # print(len(self.arr))
            for _ in range(len(self.arr)):
                p = self.arr.pop(0)
                # print(p.data)
                visited.add(p)
                if self.rootMap[p] and self.rootMap[p] not in visited:
                    self.arr.append(self.rootMap[p]); visited.add(self.rootMap[p])
                if p.left and p.left not in visited: self.arr.append(p.left); visited.add(p.left)
                if p.right and p.right not in visited: self.arr.append(p.right); visited.add(p.right)
            res += 1
        
        return res





#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends