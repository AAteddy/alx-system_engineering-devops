#!/usr/bin/python3
"""Exports to-do list information of all employees to a JSON format.
"""

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users').json()
    todos = requests.get(url + 'todos').json()

    with open("todo_all_employees.json", "w", newline="") as json_dict:
        for employee in user:
            json.dump({employee.get('id'):
                    [{"username": employee.get('username'), 
                        "task": td.get('title'), 
                        "completed": td.get('completed')} 
                    for td in todos]}, json_dict)
