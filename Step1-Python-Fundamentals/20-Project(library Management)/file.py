"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


PATH = 'C:/Users/Zanis/Desktop/content.txt'

import os
# delete file ---> os.remove()

if os.path.exists(PATH):
    print("yes")
else:
    print("no")
# delete folder --> os.rmdir()