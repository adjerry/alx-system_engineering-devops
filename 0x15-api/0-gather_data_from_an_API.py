#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com REST API for a given employee ID
to return information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    userID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userID)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(userID)).json()
    completed_tasks = []
    for task in todos:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todos)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
