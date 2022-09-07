from github import Github

token = open('TOKEN.txt', 'r').read()

g = Github(token)


def get_followers():
    return g.get_user().followers


def get_repos():
    repos = []
    for repo in g.get_user().get_repos():
        repos.append(repo.full_name)
    return len(repos)
