#!/usr/bin/python3
"""
Fetches data from an API
and returns information about the employee's todo list progress
"""

import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    completed_tasks = []
    user_name = user.get('name').strip()
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user_name, len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
