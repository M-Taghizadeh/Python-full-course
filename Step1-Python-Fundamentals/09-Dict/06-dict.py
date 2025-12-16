"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


### [DICTIONARY]
# A dictionary is a collection which is unordered, changeable and indexed. (Key Value Data Structure...)

# define
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# get value
x = thisdict.get("model")
print(thisdict['brand'])

# len
print(len(thisdict))

# change value
thisdict['year'] = '2019'

# del remove copy ,....