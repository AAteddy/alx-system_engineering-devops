#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the 
number of subscribers on a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers on a
    given subreddit.
    OR - Returns 0 if not a valid subreddit.
    """
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'User-Agent': 'CustomUserAgent'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)

    result = response

    try:
        # grab the info about the users' tasks
        data = result.get('data')
        subscribers = data.get('subscribers')
    except:
        return 0
    if subscribers is None:
        return 0
    return int(subscribers)
