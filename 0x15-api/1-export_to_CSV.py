#!/usr/bin/python3
"""For a given employee ID, returns TODO list info as CSV format"""
if __name__ == "__main__":
    """ __main__ """

    import csv
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

    fp = empID + ".csv"
    with open(fp, "w") as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csvWriter.writerow(
                [empID, username, todo.get("completed"), todo.get("title")])
