"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
  f = open('file.txt', 'r')
except:
  print("this file not exist!!!!")
finally:
  print("The 'try except' is finished")

