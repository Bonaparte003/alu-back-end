#!/usr/bin/python3
"""Script to gather data from an API"""


import json
import requests


def main():
    """main function"""
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_data = requests.get(users_url).json()
    todos_data = requests.get(todos_url).json()

    all_tasks = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']
        user_tasks = []

        for task in todos_data:
            if task['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                user_tasks.append(task_info)
        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f, indent=4)


if __name__ == "__main__":
    main()
