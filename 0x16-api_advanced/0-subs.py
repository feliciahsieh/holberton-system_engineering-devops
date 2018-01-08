#!/usr/bin/python3
"""0-subs.py - Query the Reddit API and print # subscribers for a subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    count = 0
    baseURL = "https://www.reddit.com/r/"
    url = baseURL + subreddit + "/about/.json"

    headers = { 'User-Agent': 'My User Agent 1.0',
                'From': '214@holbertonschool.com'
    }
    result = requests.get(url, headers=headers).json()

    count = result['data']['subscribers']
    return count
