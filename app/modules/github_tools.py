import json
import time
from github import Github

token = open('TOKEN.txt', 'r').read()

g = Github(token)


def count_repos() -> int:
    """Function to get user repos"""

    return len(list(g.get_user().get_repos()))


def count_stars() -> int:
    """Function to get user stars"""

    global_stars = 0
    for repo in g.get_user().get_repos():
        global_stars += repo.stargazers_count
    return global_stars


def count_subscribers() -> int:
    """Function to get subscribers"""

    return g.get_user().followers


def set_profile_data():
    """Function to set profile data"""

    json.dump(
        {'followers': count_subscribers(), 'stars': count_stars(), 'repos': count_repos()},
        open('app/data/github_profile.json', 'w')
    )
    time.sleep(3600)


def get_profile_data() -> dict:
    """Function to get profile data from json"""

    return json.load(open('app/data/github_profile.json', 'r'))
