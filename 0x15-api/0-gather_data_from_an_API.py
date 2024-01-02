#!/usr/bin/python3
"""Accessing a REST API's url and returns todo-list information
for a given employee id.
"""

import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    completed = [td.get('title') for td in todos if td.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
            .format(user.get('name'), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]

