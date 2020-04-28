from Queue import Queue


class Breadth:
    def __init__(self, start, goal):
        self.start = start
        self.start.visited = True
        self.goal = goal
        self.border = Queue(20)
        self.border.enqueue(start)
        self.found = False
        self.visited_cities = []

    def search(self):
        first = self.border.getFirst()
        self.visited_cities.append(first.name)

        if first == self.goal:
            self.found = True
        else:
            self.border.dequeue()
            for a in first.adjacent:
                if a.city.visited == False:
                    a.city.visited = True
                    self.border.enqueue(a.city)
            if self.border.numberElements > 0:
                Breadth.search(self)
        return self.visited_cities
