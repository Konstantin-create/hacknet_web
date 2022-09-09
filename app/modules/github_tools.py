import json
from github import Github
from datetime import datetime, timedelta

token = open('TOKEN.txt', 'r').read()

g = Github(token)


def set_statistics():
    last_update = datetime.utcnow()
    while True:
        if (datetime.utcnow() - last_update) > timedelta(hours=1):
            last_update = datetime.utcnow()
            json.dump((get_stars(), get_followers(), get_repos()), open('../data/github_stat.json', 'w'))


def get_statistic():
    return json.load(open('../data/github_stat.json'))


def get_followers() -> int:
    """Function to count my followers"""

    return g.get_user().followers


def get_repos() -> int:
    """Function to count my repos"""

    repos = []
    for repo in g.get_user().get_repos():
        repos.append(repo.full_name)
    return len(repos)


def get_stars() -> int:
    """Function to count total stars"""

    repos = list(g.get_user().get_repos())
    total = 0
    for repo in repos:
        total += repo.stargazers_count
    return total
