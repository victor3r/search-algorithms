from Stack import Stack


class Depth:
    def __init__(self, start, goal):
        self.start = start
        self.start.visited = True
        self.goal = goal
        self.border = Stack(20)
        self.border.push(start)
        self.found = False
        self.visited_cities = []

    def search(self):
        top = self.border.getTop()
        self.visited_cities.append(top.name)

        if top == self.goal:
            self.found = True
        else:
            for a in top.adjacent:
                if self.found == False:
                    if a.city.visited == False:
                        a.city.visited = True
                        self.border.push(a.city)
                        Depth.search(self)
        return self.visited_cities
