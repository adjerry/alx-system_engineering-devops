#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com REST API and a given employee ID to
record all tasks that are owned by this employee in a JSON file
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    userID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userID)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(userID)).json()
    username = user.get('username')
    tasks = []
    for task in todos:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[userID] = tasks
    with open("{}.json".format(userID), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
