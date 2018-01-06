#!/usr/bin/python3

import json
import requests
import sys

if __name__ == "__main__":
    """ __main__ """

    def top_ten(subreddit):
        url = "https://www.reddit.com/dev/api/"

        urlNew = url + 'users/'
        return requests.get(urlNew + subreddit).json()
