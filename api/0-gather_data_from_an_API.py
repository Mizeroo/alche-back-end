#!/usr/bin/python3
"""Module that gathers data about an employee's TODO list progress
from a REST API.
"""
import sys

import requests

employee_id = int(sys.argv[1])
BASE_URL = 'https://jsonplaceholder.typicode.com'

r = requests.get("{}/users/{}".format(BASE_URL, employee_id))
data = r.json()
employee_name = data["name"]

todos_r = requests.get(
    "{}/todos".format(BASE_URL),
    params={"userId": employee_id}
)
todos_data = todos_r.json()
total_tasks = len(todos_data)

completed_task = []
for task in todos_data:
    if task['completed']:
        completed_task.append(task)
number_done = len(completed_task)

print("Employee {} is done with tasks({}/{}):".format(
    employee_name, number_done, total_tasks))
for task in completed_task:
    print("\t {}".format(task['title']))
