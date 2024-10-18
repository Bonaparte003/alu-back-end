#!/usr/bin/python3
"""Script that fetches data from an API"""


import requests
import sys


def main():
    """Fetches data from an API"""
    inid = int(sys.argv[1])
    user_url = f'https://jsonplaceholder.typicode.com/users?id={inid}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={inid}'
    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()

    user_name = user_data[0]['name']
    user_username = user_data[0]['username']
    counter_done = 0
    counter_total = len(todo_data)
    list_done = []

    for task in todo_data:
        if task['completed']:
            counter_done += 1
            list_done.append(task['title'])

    print(f'Employee {user_name} {user_username} is done with tasks '
          f'({counter_done}/{counter_total}):')
    for task_title in list_done:
        print(f'\t {task_title}')


if __name__ == "__main__":
    main()
