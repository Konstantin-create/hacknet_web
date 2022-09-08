from github import Github

token = open('TOKEN.txt', 'r').read()

g = Github(token)


def get_statistics():
    pass


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
