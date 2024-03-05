#!/usr/bin/python3
"""A function that queries the Reddit API and returns the 
number of subscribers on a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers on a given subreddit.
    OR - Returns 0 if not a valid subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "CustomUserAgent/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    else:
        return 0
