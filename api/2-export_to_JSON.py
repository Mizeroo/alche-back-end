#!/usr/bin/python3
"""Module that exports an employee's TODO list data to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    r = requests.get("{}/users/{}".format(BASE_URL, employee_id))
    data = r.json()
    username = data["username"]

    todos_r = requests.get(
        "{}/todos".format(BASE_URL),
        params={"userId": employee_id}
    )
    todos_data = todos_r.json()

    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })

    all_data = {str(employee_id): tasks_list}

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as jsonfile:
        json.dump(all_data, jsonfile)
