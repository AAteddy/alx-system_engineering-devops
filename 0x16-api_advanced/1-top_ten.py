#!/usr/bin/python3
"""A function that queries the Reddit API and returns 
the titles of the first 10 hot posts listed.
"""
import requests

headers = {"User-Agent": "CustomUserAgent/1.0"}

def top_ten(subreddit):
    """Returns the titles of the first 10 hot posts listed
    for a given subreddit.
    OR - Returns 0 if not a valid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = { "limit": 10 }

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        result = response.json()
        for post in result["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
