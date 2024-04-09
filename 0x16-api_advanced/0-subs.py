#!/usr/bin/python3
"""
    this module contains the function number_of_subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
        queries the Reddit API for a given subreddit.
    :param subreddit: the subreddit to handle.
    :return: The number of subscribers (not active users, total subscribers).
             If an invalid subreddit is given, the function should return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # A unique User-Agent header to identify the client
    headers = {'User-Agent': 'sitawi/0.0.14'}
    response = requests.get(url, headers=headers, allow_redirects=False).json()

    try:
        return response.get('data').get('subscribers')
    except Exception:
        return 0
