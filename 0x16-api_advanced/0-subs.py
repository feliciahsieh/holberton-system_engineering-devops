#!/usr/bin/python3

import json
import requests
import sys

if __name__ == "__main__":
    """ __main__ """

    def number_of_subscribers(subreddit):
        url = "https://www.reddit.com/dev/api/"

        urlUsers = url + 'users/'
        return requests.get(urlUsers + subreddit).json()
