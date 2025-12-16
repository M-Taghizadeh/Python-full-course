"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


class Person:
    count = 0
    # Create New Object(Constructor)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1 

    def get_name(self):
        print("name is %s" %self.name)
    
    def get_age(self):
        print("age is %s" %self.age)

    def get_info(self):
        print("name is %s and age is %s" %(self.name, self.age))

    def get_count(self):
        print(Person.count)

# new object:
p1 = Person("amir reza", 21)
p2 = Person("ahmad", 22)

p1.get_age()
p2.get_age()
p2.get_name()
p1.get_info()
p1.get_count()


