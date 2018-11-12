import requests
import json
import os


list_of_pull_requests = []


def get_pull_requests(username, repository):

    github_url = "https://api.github.com"
    r = requests.get(os.path.join(github_url, "repos", repository, "pulls"))
    js = json.loads(r.content)
    for pull in js:
        if username == pull['user']['login']:
            if 'title' in pull.keys():
                list_of_pull_requests.append(pull['title'])
    return list_of_pull_requests
