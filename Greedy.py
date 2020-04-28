from OrderedVector import OrderedVector


class Greedy:
    def __init__(self, goal):
        self.goal = goal
        self.found = False
        self.travelled_distance = 0
        self.previous = None
        self.visited_cities = []

    def search(self, current):
        current.visited = True
        self.visited_cities.append(current.name)
        for a in current.adjacent:
            if a.city == self.previous:
                self.travelled_distance += a.distance
        self.previous = current

        if current == self.goal:
            self.found = True
        else:
            self.border = OrderedVector(len(current.adjacent))
            for a in current.adjacent:
                if a.city.visited == False:
                    a.city.visited = True
                    self.border.insert(a.city)
            if self.border.getFirst() != None:
                Greedy.search(self, self.border.getFirst())
        return (self.visited_cities, self.travelled_distance)
