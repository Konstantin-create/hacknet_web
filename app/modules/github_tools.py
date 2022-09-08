from github import Github
from datetime import datetime

token = open('TOKEN.txt', 'r').read()

g = Github(token)


def get_statistics():
    last_update = datetime.utcnow()
    while True:
        print(datetime.utcnow() - last_update)
        if (datetime.utcnow() - last_update) > 60:
            last_update = datetime.utcnow()
            return get_stars(), get_followers(), get_repos()


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

get_statistics()