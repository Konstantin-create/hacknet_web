import json
import markdown
from github import Github
from datetime import datetime, timedelta

token = open('TOKEN.txt', 'r').read()

g = Github(token)
pinned_projects = ['Konstantin-create/VCS', 'Konstantin-create/cSc-chat', 'Konstantin-create/DataStructures']


def set_statistics() -> None:
    """Function to get global profile statistics"""

    last_update = datetime.utcnow()
    while True:
        if (datetime.utcnow() - last_update) > timedelta(hours=1):
            last_update = datetime.utcnow()
            json.dump((get_stars(), get_followers(), get_repos()), open('app/data/github_stat.json', 'w'), indent=4)


def get_statistic() -> list:
    """Function to get global profile statistics from local storage"""

    return json.load(open('app/data/github_stat.json'))


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


def set_pinned_repos() -> None:
    """Function to parse pinned repos"""

    last_update = datetime.utcnow()
    while True:
        if (datetime.utcnow() - last_update) > timedelta(hours=1):
            last_update = datetime.utcnow()

            output = []
            for repo in pinned_projects:
                repo_obj = g.get_repo(repo)
                output.append({
                    'name': repo[:repo.rfind('/')],
                    'description': repo_obj.description,
                    'stars': repo_obj.stargazers_count,
                    'language': repo_obj.language
                })
            json.dump(output, open('app/data/github_pinned.json', 'w'), indent=4)


def get_pinned_repos() -> list:
    """Function to get pinned repos data from local storage"""

    return json.load(open('app/data/github_pinned.json', 'r'))


def set_user_description() -> None:
    """Function to get user description"""

    last_update = datetime.utcnow()
    while True:
        if (datetime.utcnow() - last_update) > timedelta(hours=1):
            last_update = datetime.utcnow()

            content = g.get_repo('Konstantin-create/Konstantin-create').get_readme().decoded_content.decode('utf-8')
            first_description = content[
                                content.find('<!---first-description-->') + len('<!---first-description-->'):
                                content.find('<!---end-->', content.find('<!---first-description-->'))
                                ]
            second_description = content[
                                 content.find('<!---second-description-->') + len('<!---second-description-->'):
                                 content.find('<!---end-->', content.find('<!---second-description-->'))
                                 ]
            open('app/templates/temp/github_about.html', 'w').write(
                markdown.markdown((first_description + second_description).replace('\\', '')))
