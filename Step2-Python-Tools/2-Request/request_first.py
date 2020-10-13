import requests
response = requests.get("https://daneshjooyar.com")
txt = response.text
print(txt)