class ProductOfNumbers:

    def __init__(self):
        self.Q = []

    def add(self, num: int) -> None:
        if num == 0:
            while self.Q: self.Q.pop(0)
            self.Q.append(num)
        else:
            if self.Q and self.Q[-1] != 0:
                self.Q.append(self.Q[-1]*num)
            else:
                self.Q.append(num)

    def getProduct(self, k: int) -> int:
        if len(self.Q) < k: return 0
        if len(self.Q)==k: 
            if self.Q[0]==0: return 0
            else: return self.Q[-1]
        return (self.Q[-1] // self.Q[-(k+1)]) if self.Q[-(k+1)] != 0 else self.Q[-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)