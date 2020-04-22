class OrderedVector:
    def __init__(self, size):
        self.numberElements = 0
        self.cities = [None] * size

    def insert(self, city):
        if self.numberElements == 0:
            self.cities[0] = city
            self.numberElements = 1
            return

        position = 0
        i = 0
        while (i < self.numberElements):
            if city.goalDistance > self.cities[position].goalDistance:
                position += 1
            i += 1

        for k in range(self.numberElements, position, -1):
            self.cities[k] = self.cities[k - 1]

        self.cities[position] = city
        self.numberElements += 1

    def getFirst(self):
        return self.cities[0]

    def show(self):
        for i in range(self.numberElements):
            print(
                '{} - {}'.format(self.cities[i].name, self.cities[i].goalDistance))
