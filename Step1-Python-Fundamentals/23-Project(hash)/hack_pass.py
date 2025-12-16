"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


import hashlib

def hash256(password):
    sha256 = hashlib.sha256(password.encode('utf-8')).hexdigest() ### sha256 is 64 chars
    return sha256
    
Fin = open("C:/Users/Zanis/Desktop/Python Docs/19-hashlib/pass.csv")

for line in Fin:
    for i in range(0, 10000):
        tmp_pass = str.format("%04d"%i)
        tmp_hash = line.split(",")
        if(hash256(tmp_pass)==tmp_hash[1].strip()):
            print("pass of %s is %s " %(tmp_hash[0],tmp_pass))
            
