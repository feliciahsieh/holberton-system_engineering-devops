#!/usr/bin/python3
"""2-recurse.py - Query Reddit API & find titles of all hot articles"""
import json
import pprint
import requests


def recurse(subreddit, hot_list=[], params={}):
    """Find hot article titles using recursion"""

    payload = {}
    pp = pprint.PrettyPrinter(indent=2)

    baseURL = "https://www.reddit.com/r/"
    url = baseURL + subreddit + "/hot/.json?limit=100"

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '214@holbertonschool.com'
    }

    result = requests.get(url, headers=headers, params=params)

    if result.status_code == 200:
        result = result.json()
        after = result.get('data').get('after')
        if after is None:
            children = result.get('data').get('children')
            title = []
            for i in range(100):
                title.append(children[i].get('data').get('title'))
                hot_list.append(title)
                pp.pprint(hot_list)
            return hot_list
        else:
            payload = {"after" : after}
            pp.pprint(payload)
            recurse(subreddit, hot_list, payload)

            children = result.get('data').get('children')
            title = []
            for i in range(100):
                title.append(children[i].get('data').get('title'))
                hot_list.append(title)
                pp.pprint(hot_list)
    else:
        print("None")
        return
