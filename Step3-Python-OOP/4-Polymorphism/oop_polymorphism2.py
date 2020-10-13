class Animal:
    def move(self):
        print("animal can move...!")

class Fish(Animal):
    def move(self):
        print("fish can swim!!!")

class Human(Animal):
    def move(self):
        print("Human can Walking!!!")

h1 = Human()
h1.move()