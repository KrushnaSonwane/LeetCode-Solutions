from sortedcontainers import SortedList
class MyCalendar(object):

    def __init__(self):
        self.nums = SortedList()

    def book(self, start, end):
        l, r = 0, len(self.nums) - 1
        while r >= l:
            mid = (r + l) // 2
            if self.nums[mid][0] <= start and self.nums[mid][1] >= start: 
                return False
            elif self.nums[mid][0] <= end - 1 and self.nums[mid][1] >= end - 1: 
                return False
            elif self.nums[mid][0] >= start and self.nums[mid][0] < end - 1: 
                return False
            elif self.nums[mid][0] > end - 1:
                r = mid - 1
            else:
                l = mid + 1
        self.nums.add([start, end - 1])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)