#!/usr/bin/python3
"""
Export data in the CSV format.

Requirements:
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""
import csv
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
            with open('{}.csv'.format(emp_id), "w") as file:
                csv_writer = csv.writer(file, delimiter=",",
                                        lineterminator="\n",
                                        quoting=csv.QUOTE_ALL
                                        )
                for task in tasks:
                    csv_writer.writerow([task['userId'],
                                         emp_name, task['completed'],
                                         task['title']]
                                        )
