#!/usr/bin/python3
"""Module that exports an employee's TODO list data to CSV format."""
import csv
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

    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task["completed"],
                task["title"]
            ])
