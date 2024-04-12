#!/usr/bin/python3
"""
Export data in the JSON format.

Requirements:
    Records all tasks from all employees
    File name must be: todo_all_employees.json
"""
import json
import requests


if __name__ == '__main__':
    REST_API = "https://jsonplaceholder.typicode.com"
    todos = requests.get('{}/todos'.format(REST_API)).json()
    users = requests.get('{}/users'.format(REST_API)).json()
    users_id = []
    all = {}
    for dic in todos:
        if dic['userId'] not in users_id:
            users_id.append(dic['userId'])
    for uid in users_id:
        username = ""
        for user in users:
            if user['id'] == uid:
                username = user['username']
                break
        tasks = [x for x in todos if x['userId'] == uid]
        user_tasks = []
        for task in tasks:
            user_tasks.append({"username": username,
                               "task": task['title'],
                               "completed": task['completed']
                               }
                              )
        all.update({uid: user_tasks})
    with open('todo_all_employees.json', "w") as file:
        file.write(json.dumps(all))
