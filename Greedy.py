from OrderedVector import OrderedVector

class Greedy:
    def __init__(self, goal):
        self.goal = goal
        self.found = False
        
    def search(self, current):
        print('\nAtual: {}'.format(current.name))
        current.visited = True
        
        if current == self.goal:
            self.found = True
        else:
            self.border = OrderedVector(len(current.adjacent))
            for a in current.adjacent:
                if a.city.visited == False:
                    a.city.visited = True
                    self.border.insert(a.city)
            self.border.show()
            if self.border.getFirst() != None:
                Greedy.search(self, self.border.getFirst())
                    