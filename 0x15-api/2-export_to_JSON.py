#!/usr/bin/python3
"""
Export data in the JSON format.

Requirements:
    Records all tasks that are owned by this employee
    File name must be: USER_ID.json
"""
import json
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
            username = req.get('username')
            tasks = [x for x in todos if x['userId'] == emp_id]
            user_tasks = []
            for task in tasks:
                user_tasks.append({"task": task['title'],
                                   "completed": task['completed'],
                                   "username": username
                                   }
                                  )
            with open('{}.json'.format(emp_id), "w") as file:
                file.write(json.dumps({emp_id: user_tasks}))
