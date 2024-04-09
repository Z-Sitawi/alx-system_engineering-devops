#!/usr/bin/python3
"""
    this module contains the function top-ten
"""
import requests


def top_ten(subreddit):
    """
        Queries the Reddit API and prints the titles of the first 10 hot posts
        listed for a given subreddit.
    :param subreddit: the subreddit to handle.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"

    # A unique User-Agent header to identify the client
    headers = {'User-Agent': 'sitawi/0.0.14'}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    try:
        for child in response['data']['children']:
            print(child.get('data')['title'])
    except Exception:
        print(None)
