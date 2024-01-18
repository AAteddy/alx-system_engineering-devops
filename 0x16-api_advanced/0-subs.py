#!/usr/bin/python3
"""A function that queries the Reddit API and returns the 
number of subscribers on a given subreddit.
"""
import requests

headers = { "User-Agent": "CustomUserAgent/1.0" }

def number_of_subscribers(subreddit):
    """Returns the total number of subscribers on a given subreddit.
    OR - Returns 0 if not a valid subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        result = response.json()
        return result["data"]["subscribers"]
    else:
        return 0
