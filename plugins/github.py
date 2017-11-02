import requests
import json
list_of_pull_requests=[]
def get_pull_requests_github(username,repository):
    r=requests.get("https://api.github.com/repos/"+username+"/"+repository+"/pulls")
    js=json.loads(r.content)
    for i in range(0,len(js)):
        if 'title' in  js[i].keys():
            list_of_pull_requests.append(js[i]['title'])
    return list_of_pull_requests


#print get_pull_requests_github(username,repository)
