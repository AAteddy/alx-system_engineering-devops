#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    with open("{}.json".format(sys.argv[1]), "w", newline="") as json_file:
        json.dump({sys.argv[1]: 
            [{"task": td.get('title'), 
                "completed": td.get('completed'), 
                "username": user.get('username')} 
                for td in todos]}, json_file)
