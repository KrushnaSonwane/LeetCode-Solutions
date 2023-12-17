from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.A, self.B, self.C = {}, {}, {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.A[f] = -r
            if c not in self.B:
                self.B[c] = SortedList()
            self.B[c].add([-r, f])
            self.C[f] = c

    def changeRating(self, food: str, newRating: int) -> None:
        r = self.A[food]
        c = self.C[food]
        self.B[c].discard([r, food])
        self.A[food] = -newRating
        self.B[c].add([-newRating, food])
        

    def highestRated(self, cuisine: str) -> str:
        return self.B[cuisine][0][-1]        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)