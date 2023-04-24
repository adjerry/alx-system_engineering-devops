#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com REST API
to record all tasks from all employees in a JSON file
"""

import json
import requests

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    userdict = {}
    usernamedict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for task in todos:
        taskdict = {}
        uid = task.get("userId")
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = usernamedict.get(uid)
        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)
