#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format.
"""

import csv
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user.get('id'), user.get('username'), td.get('completed'), td.get('title')]
            ) for td in todos]
        file.close()
