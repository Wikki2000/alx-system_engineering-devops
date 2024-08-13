#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """
    # set custom user-agent
    user_agent = 'wikki'
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # custom user-agent avoids request limit
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    # load response data from json
    data = r.json().get('data', {})

    # return number of subreddit subscribers
    return data.get('subscribers', 0)
