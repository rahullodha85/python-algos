class Animal:

    def __init__(self, n: str):
        self.name = n

    def set_order(self,ord):
        self.order = ord

    def get_order(self):
        return self.order

    def is_older(self, a):
        return self.order < a.get_order()

    def get_name(self):
        return self.name

class Dog(Animal):

    def __init__(self, n):
        super().__init__(n)

class Cat(Animal):
    def __init__(self, n):
        super().__init__(n)

class AnimalQueue:

    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, a: Animal):
        a.set_order(self.order)
        self.order +=1

        if isinstance(a, Dog):
            self.dogs.append(a)
        if isinstance(a, Cat):
            self.cats.append(a)

    def dequeue_any(self):

        if len(self.dogs) == 0:
            return self.dequeue_cats()
        if len(self.cats) == 0:
            return self.dequeue_dogs()

        dog = self.dogs[0]
        cat = self.cats[0]

        if dog.is_older(cat):
            return self.dequeue_dogs()
        else:
            return self.dequeue_cats()

    def dequeue_dogs(self):
        return self.dogs.pop(0)

    def dequeue_cats(self):
        return self.cats.pop(0)

queue = AnimalQueue()
queue.enqueue(Dog('nimko'))
queue.enqueue(Cat('lucky'))
queue.enqueue(Dog('rocky'))
queue.enqueue(Cat('grey'))

print(queue.dequeue_dogs().name)
print(queue.dequeue_any().name)
print(queue.dequeue_dogs().name)
print(queue.dequeue_cats().name)
