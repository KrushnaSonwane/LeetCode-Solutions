class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.a = big
        self.b = medium
        self.c = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.a:
            self.a -= 1
            return 1
        elif carType == 2 and self.b:
            self.b -= 1
            return 1
        elif carType == 3 and self.c:
            self.c -= 1
            return 1
        else:
            return 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)