#!/usr/bin/python3
"""For a given employee ID, returns TODO list info as JSON format"""
import collections
import csv
import json
import requests
import sys

if len(sys.argv) != 1:
    exit(1)

url = 'https://jsonplaceholder.typicode.com/'

urlUser = url + 'users/'
urlTodos = url + 'todos/'

users = requests.get(urlUser).json()
todos = requests.get(urlTodos).json()

if (len(users) == 0):
    exit(1)

data = collections.OrderedDict()
values = []

for user in users:
    username = user.get("username")
    for todo in todos:
        t = collections.OrderedDict()
        t["username"] = username
        t["task"] = todo.get("title")
        t["completed"] = todo.get("completed")
        values.append(t)
        data["1"] = values

filename = "todo_all_employees.json"
with open(filename, "w") as fp:
    fp.write(json.dumps(data))
