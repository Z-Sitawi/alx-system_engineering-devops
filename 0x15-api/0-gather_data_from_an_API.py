#!/usr/bin/python3
"""
This script accepts an integer as a parameter, which is the employee ID.
Then, returns information about his/her to_do list progress.
"""
from requests import get
from sys import argv

REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(argv) > 1:
        if argv[-1].isnumeric():
            emp_id = int(argv[1])
            req = get(f'{REST_API}/users/{emp_id}').json()
            todos = get(f'{REST_API}/todos/').json()
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
                    print(f'\t{task["title"]}')
