#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com REST API with a given imployee ID
Records all tasks that are owned by this employee in CSV file.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    userID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userID)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(userID)).json()
    with open("{}.csv".format(userID), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            taskwriter.writerow([int(userID),
                                user.get('username'),
                                task.get('completed'),
                                task.get('title')])
