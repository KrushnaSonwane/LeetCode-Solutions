#User function Template for python3

class TwoStacks:
    def __init__(self, n=100):
        self.A = []
        self.B = []
        self.n = n

    # Function to push an integer into stack 1
    def push1(self, x):
        self.A.append(x)
            

    # Function to push an integer into stack 2
    def push2(self, x):
        self.B.append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.A: return self.A.pop()
        return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.B: return self.B.pop()
        return -1



#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        sq = TwoStacks()
        Q = int(input())
        while Q > 0:
            query = list(map(int, input().split()))
            if query[1] == 1:
                if query[0] == 1:
                    sq.push1(query[2])
                elif query[0] == 2:
                    sq.push2(query[2])
            elif query[1] == 2:
                if query[0] == 1:
                    print(sq.pop1(), end=' ')
                elif query[0] == 2:
                    print(sq.pop2(), end=' ')
            Q -= 1
        print()
        T -= 1

# } Driver Code Ends