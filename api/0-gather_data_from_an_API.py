#!/usr/bin/python3
import requests
import sys

employee_id = int(sys.argv[1])
BASE_URL ='https://jsonplaceholder.typicode.com'
r = requests.get("{}/users/{}".format(BASE_URL, employee_id))
data=r.json()
employee_name = data["name"]
#print(employee_name)

todos_r = requests.get("{}/todos".format(BASE_URL), params={"userId": employee_id})

todos_data = todos_r.json()
total_tasks =len(todos_data)
#print(todos_data)
completed_task = []

for task in todos_data:
	if task['completed'] == True:
		completed_task.append(task)

number_done = len(completed_task)

print("Employee {} is done with tasks({}/{}):".format(employee_name, number_done, total_tasks))
for task in completed_task:
    print("\t {}".format(task['title']))
#print(completed_task)
#print(number_done)
