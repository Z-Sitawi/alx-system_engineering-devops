#!/usr/bin/python3
"""
this module contains top_ten function
"""
import requests

headers = {"User-Agent": "SitawiZak/1.0"}


def top_ten(subreddit):
    """method doc"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
