import requests
import json
import utils

BASE_URL = "https://api.github.com/repos/"

@utils.safe_error_decorator
def get_pull_requests(username,repository):
    
    list_of_pulls = []
    r = requests.get(BASE_URL + "/%s/%s/pulls" % (username, repository))

    if r.status_code != 200:
        raise utils.FetchError(r, "Non 200 status code")

    else:
        js=json.loads(r.content)
        for i in range(0,len(js)):
            if 'title' in  js[i].keys():
                list_of_pulls.append(js[i]['title'])
    return list_of_pulls


#print get_pull_requests(username,repository)
