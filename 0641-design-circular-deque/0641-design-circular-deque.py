class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.queue = deque()

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.size:
            self.queue.appendleft(value)
            return 1
        return 0

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.size:
            self.queue.append(value)
            return 1
        return 0
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.queue:
            self.queue.popleft()
            return 1
        return 0

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.queue:
            self.queue.pop()
            return 1
        return 0

    def getFront(self):
        """
        :rtype: int
        """
        if self.queue: return self.queue[0]
        return -1

    def getRear(self):
        """
        :rtype: int
        """
        if self.queue: return self.queue[-1]
        return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return not len(self.queue)

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.queue) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()