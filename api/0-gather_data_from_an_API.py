#!/usr/bin/python3
"""Fetch data from an API"""

import requests
import sys


def main():
    """the main function"""
    uid = int(sys.argv[1])
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(uid)

    response = requests.get(todos_url)

    total_questions = 0
    completed = []
    for todo in response.json():

        if todo['userId'] == uid:
            total_questions += 1

            if todo['completed']:
                completed.append(todo['title'])

    user_name = requests.get(users_url).json()['name']

    printer = ("Employee {} is done with tasks({}/{}):".format(user_name,
               len(completed), total_questions))
    print(printer)
    for t in completed:
        print("\t {}".format(t))


if __name__ == '__main__':
    main()
