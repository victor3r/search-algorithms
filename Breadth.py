from Queue import Queue


class Breadth:
    def __init__(self, start, goal):
        self.start = start
        self.start.visited = True
        self.goal = goal
        self.border = Queue(20)
        self.border.enqueue(start)
        self.found = False

    def search(self):
        first = self.border.getFirst()
        print('Primeiro: {}'.format(first.name))

        if first == self.goal:
            self.found = True
        else:
            temp = self.border.dequeue()
            print('Desenfileirou: {}'.format(temp.name))
            for a in first.adjacent:
                print('Verificando se já visitado: {}'.format(a.city.name))
                if a.city.visited == False:
                    a.city.visited = True
                    self.border.enqueue(a.city)
            if self.border.numberElements > 0:
                Breadth.search(self)
