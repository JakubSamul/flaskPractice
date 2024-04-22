import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes:": 78, "name": "Joe", "views": 100000}, 
        {"likes:": 87, "name": "Jacoboo", "views": 6000},
        {"likes:": 10, "name": "Tim", "views": 700}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())