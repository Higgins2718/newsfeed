import requests

r = requests.post(url = "https://lambdanewsfeedproject.herokuapp.com/api/", data = "smart chips artificial intelligence")
#r = requests.post(url = "http://127.0.0.1:5000/api/", data = "tennis football")

print(r.content)