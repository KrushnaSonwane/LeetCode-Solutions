"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashT = defaultdict(int)
        for obj in employees: hashT[obj.id] = obj
        def dfs(id):
            return sum(dfs(child) for child in hashT[id].subordinates) + hashT[id].importance
        return dfs(id)