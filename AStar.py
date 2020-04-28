from AdjacentOrderedVector import AdjacentOrderedVector


class AStar:
    def __init__(self, goal):
        self.goal = goal
        self.found = False
        self.travelled_distance = 0
        self.previous = None
        self.visited_cities = []

    def search(self, current):
        self.visited_cities.append(current.name)
        current.visited = True
        for a in current.adjacent:
            if a.city == self.previous:
                self.travelled_distance += a.distance
        self.previous = current

        if current == self.goal:
            self.found = True
        else:
            self.border = AdjacentOrderedVector(len(current.adjacent))
            for a in current.adjacent:
                if a.city.visited == False:
                    a.city.visited = True
                    self.border.insert(a)
            if self.border.getFirst() != None:
                AStar.search(self, self.border.getFirst())
        return (self.visited_cities, self.travelled_distance)
