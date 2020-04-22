class Queue:
    def __init__(self, size):
        self.size = size
        self.cities = [None] * self.size
        self.start = 0
        self.end = -1
        self.numberElements = 0

    def enqueue(self, city):
        if not Queue.fullQueue(self):
            if self.end == self.size - 1:
                self.end = -1
            self.end += 1
            self.cities[self.end] = city
            self.numberElements += 1
        else:
            print("A fila já está cheia")

    def dequeue(self):
        if not Queue.emptyQueue(self):
            temp = self.cities[self.start]
            self.start += 1
            if self.start == self.size:
                self.start = 0
            self.numberElements -= 1
            return temp
        else:
            print("A fila já está vazia")

    def getFirst(self):
        return self.cities[self.start]

    def emptyQueue(self):
        return self.numberElements == 0

    def fullQueue(self):
        return self.numberElements == self.size
