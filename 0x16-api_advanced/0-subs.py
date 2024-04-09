#!/usr/bin/python3
""" this model defines a function that queries the Reddit API
and returns the number of subscribers (not active users, total subscribers)
for a given subreddit.
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
    headers = {'User-Agent': 'MyBot/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        subscribers = data['data']['subscribers']

        return subscribers
    elif response.status_code == 404:  # Subreddit not found
        return 0
    else:
        return 0
