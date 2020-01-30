import requests

r = requests.post(url = "https://comakecategorizer.herokuapp.com/api/", data = "technology can be interesting")
print(r.content)