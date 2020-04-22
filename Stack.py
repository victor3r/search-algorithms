class Stack:
    def __init__(self, size):
        self.size = size
        self.cities = [None] * self.size
        self.top = -1

    def push(self, city):
        if not Stack.fullStack(self):
            self.top += 1
            self.cities[self.top] = city
        else:
            print("A pilha já está cheia")

    def pop(self):
        if not Stack.emptyStack(self):
            temp = self.cities[self.top]
            self.top -= 1
            return temp
        else:
            print("A pilha já está vazia")

    def getTop(self):
        return self.cities[self.top]

    def emptyStack(self):
        return self.top == -1

    def fullStack(self):
        return self.top == self.size - 1
