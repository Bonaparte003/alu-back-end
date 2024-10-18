#!/usr/bin/python3
"""Script to gather data from an API"""

import requests
import sys


def main():
    """main function"""
    inid = int(sys.argv[1])
    user_url = f'https://jsonplaceholder.typicode.com/users?id={inid}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={inid}'
    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()
    counter_done = 0
    counter_total = 0
    list_done = []
    user_names = f"{user_data[0]['name']} {user_data[0]['username']}"
    for i in todo_data:
        if i['completed'] is True:
            counter_done += 1
            list_done.append(i['title'])

    for a in todo_data:
        if a['completed'] is True or a['completed'] is False:
            counter_total += 1

    print(f'Employee {user_names} is done with tasks '
          f'({counter_done}/{counter_total}):')
    for j in list_done:
        print('\t {}'.format(j))

    with open("./{}.csv".format(inid), "w") as f:
        with open("./{}.csv".format(inid), "w") as f:
            for i in todo_data:
                data_string = (
                    f"{inid},{user_data[0]['username']},"
                    f"{i['completed']},{i['title']}"
                )
                f.write(data_string)
                f.write("\n")


if __name__ == "__main__":
    main()
