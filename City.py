class City:
    def __init__(self, name, goalDistance):
        self.name = name
        self.visited = False
        self.goalDistance = goalDistance
        self.adjacent = []

    def addAdjacentCity(self, adjacent):
        self.adjacent.append(adjacent)
