class Adjacent:
    def __init__(self, city, distance):
        self.city = city
        self.distance = distance
        self.AStarDistance = self.city.goalDistance + self.distance
