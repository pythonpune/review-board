import requests
import json
import os


list_of_pull_requests=[]

def get_pull_requests(username,repository):
    github_url = "https://api.github.com"
    r = requests.get(os.path.join(github_url, "repos", repository, "pulls"))
    js = json.loads(r.content)
    for i in range(0, len(js)):
        if username == js[i]['user']['login']:
            if 'title' in js[i].keys():
                list_of_pull_requests.append(js[i]['title'])
    return list_of_pull_requests
