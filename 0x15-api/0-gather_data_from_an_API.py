#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    response1 = requests.get(user)
    json_file = response1.json()
    print("Employee {} is done with tasks".format(
        json_file.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    response2 = requests.get(todos)
    tasks = response2.json()
    completed_task = []
    for task in tasks:
        if task.get('completed') is True:
            completed_task.append(task)

    print("({}/{}):".format(len(completed_task), len(tasks)))
    for task in completed_task:
        print("\t {}".format(task.get("title")))
