#!/usr/bin/python3
"""A function that queries the Reddit API and returns the 
number of subscribers on a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers on a given subreddit.
    OR - Returns 0 if not a valid subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = { "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)" }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subscribers")
