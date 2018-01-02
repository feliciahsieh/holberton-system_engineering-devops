#!/usr/bin/python3
"""For a given employee ID, returns TODO list info"""
import json
import sys
import requests

empID = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/'

url_empID = url + 'users?id=' + str(empID)
user = requests.get(url_empID)
userJson = user.json()
empName = userJson[0]["name"]

url_TodoCompleted = url + 'todos?userId=' + empID + '&completed=true'
t = requests.get(url_TodoCompleted)
tJson = t.json()
nTodoDone = len(tJson)

url_TodoTotal = url + 'todos?userId=' + empID
tot = requests.get(url_TodoTotal)
totJson = tot.json()
nTodo = len(totJson)

print("Employee {} is done with tasks({}/{}):".format(empName, nTodoDone, nTodo))
for i in range(nTodoDone):
    print("\t{}".format(tJson[i]["title"]))
