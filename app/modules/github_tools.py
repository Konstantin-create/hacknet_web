from github import Github

token = open('TOKEN.txt', 'r').read()

g = Github()

print(g.get_user())