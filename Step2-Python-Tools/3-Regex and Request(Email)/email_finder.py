"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


import requests
import re

url = "http://m-taghizadeh.ir"
response = requests.get(url)
print(response)
str_site = response.text


email_list = []
email_list = re.findall("[a-zA-Z0-9.]+@[a-zA-Z]+.[a-zA-Z]+" , str_site)
print(email_list)
