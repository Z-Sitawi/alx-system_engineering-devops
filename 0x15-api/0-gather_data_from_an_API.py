#!/usr/bin/python3
"""
This script accepts an integer as a parameter, which is the employee ID.
Then, returns information about his/her to_do list progress.
"""
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            emp_id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(REST_API, emp_id)).json()
            todos = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = req.get('name')
            tasks = [x for x in todos if x['userId'] == emp_id]
            completed_tasks = [x for x in tasks if x['completed'] is True]
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
