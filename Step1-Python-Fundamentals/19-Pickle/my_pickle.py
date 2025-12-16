"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


import pickle

# dump()
my_dict = {
    "name":"mohammad",
    "family":"taghizadeh",
    "age":"22"
}
f = open("C:/Users/Zanis/Desktop/first_binary.dat", "wb")
pickle.dump(my_dict, f)


# load()
f = open("C:/Users/Zanis/Desktop/first_binary.dat", "rb")
my_dict = pickle.load(f)