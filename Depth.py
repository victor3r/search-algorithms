from Stack import Stack


class Depth:
    def __init__(self, start, goal):
        self.start = start
        self.start.visited = True
        self.goal = goal
        self.border = Stack(20)
        self.border.push(start)
        self.found = False

    def search(self):
        top = self.border.getTop()
        print('Topo: {}'.format(top.name))

        if top == self.goal:
            self.found = True
        else:
            for a in top.adjacent:
                if self.found == False:
                    print('Verificando se já visitado: {}'.format(a.city.name))
                    if a.city.visited == False:
                        a.city.visited = True
                        self.border.push(a.city)
                        Depth.search(self)
        print('Desempilhou: {}'.format(self.border.pop().name))
