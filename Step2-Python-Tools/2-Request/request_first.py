"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


import requests
response = requests.get("https://daneshjooyar.com")
txt = response.text
print(txt)