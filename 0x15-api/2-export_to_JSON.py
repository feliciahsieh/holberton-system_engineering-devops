#!/usr/bin/python3
"""For a given employee ID, returns TODO list info as JSON format"""
import collections
import csv
import json
import sys
import requests

if len(sys.argv) != 2:
    exit(1)

url = 'https://jsonplaceholder.typicode.com/'
empID = sys.argv[1]

urlUser = url + 'users/' + empID
urlTodos = url + 'todos?userId=' + empID

user = requests.get(urlUser).json()
todos = requests.get(urlTodos).json()

if (len(user) == 0):
    exit(1)

username = user.get("username")

data = {}
values = []

for todo in todos:
    t = {}
    t["task"] = todo.get("title")
    t["completed"] = todo.get("completed")
    t["username"] = username
    values.append(t)
    data[empID] = values

print("DATA: " + str(data))

fp = empID + ".csv"
with open(fp, "w") as fp:
    fp.write(str(data))
