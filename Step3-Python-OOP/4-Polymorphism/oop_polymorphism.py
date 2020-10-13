class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def __str__(self):
        return self.first + " " + self.last + " " + str(self.age)


class Employee(Person):

    # overriding:
    def __init__(self, first, last, age, salary):
        super().__init__(first, last, age)
        self.salary = salary
    
    # overriding:
    def __str__(self):
        return super().__str__() + " " + str(self.salary)
        

p1 = Person("ahmad", "mosavi", 31)
print(p1)

e1 = Employee("mohammad", 'taghizadeh', 22, 1000)
print(e1)