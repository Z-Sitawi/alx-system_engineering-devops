#!/usr/bin/python3
"""
this module contains number_of_subscribers method
"""
import requests

headers = {"User-Agent": "SitawiZakaria/1.0"}


def number_of_subscribers(subreddit):
    """ eturns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
