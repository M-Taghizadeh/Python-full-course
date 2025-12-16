"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


# An iterator is an object that contains a countable number of values.

message = "python"
myit = iter(message)

print(next(myit))
print(next(myit))

# for loop:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
