#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import csv
from urllib import response
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    response1 = requests.get(user)
    json_file = response1.json()
    name = json_file.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    response2 = requests.get(todos)
    tasks = response2.json()
    completed_task = []
    for task in tasks:
        completed_task.append([userid,
                               name,
                               task.get('completed'),
                               task.get('title')])

    new_csv_filename = '{}.csv'.format(userid)
    with open(new_csv_filename, mode='w') as employee_file:
        writer = csv.writer(employee_file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in completed_task:
            writer.writerow(task)
