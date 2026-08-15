#!/usr/bin/python3
"""Module that exports all employees' TODO list data to JSON format."""
import json
import requests


if __name__ == "__main__":
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    users_r = requests.get("{}/users".format(BASE_URL))
    users_data = users_r.json()

    all_data = {}

    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        todos_r = requests.get(
            "{}/todos".format(BASE_URL),
            params={"userId": user_id}
        )
        todos_data = todos_r.json()

        tasks_list = []
        for task in todos_data:
            tasks_list.append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            })

        all_data[str(user_id)] = tasks_list

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(all_data, jsonfile)
