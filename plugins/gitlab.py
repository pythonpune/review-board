import requests
import json
import os


def get_merge_requests(username, repository):
    """
    Get list of merge requests by username
    :param username: user on GitLab
    :param repository: Gitlab repo, example: gitlab-org/gitlab-ce
    :returns: List of titles of MRs raised by user
    """
    gitlab_url = "https://gitlab.com/api/v4/projects"
    org_name, repo_name = repository.split('/')

    # Get project-id
    project = requests.get(os.path.join(gitlab_url, org_name + "%2F" + repo_name))
    project_js = json.loads(project.content)

    # https://docs.gitlab.com/ee/api/merge_requests.html
    merge_requests = requests.get(os.path.join(gitlab_url, str(project_js['id']), 'merge_requests'))
    merge_requests_js = json.loads(merge_requests.content)

    # TODO: Currently it gets only limited number of items (default: 20)
    # Use pagination to get all merge requests, https://docs.gitlab.com/ee/api/README.html#pagination

    list_of_merge_requests = []
    for mr in merge_requests_js:
        if (mr.get('author').get('username') == username):
            list_of_merge_requests.append(mr['title'])

    return list_of_merge_requests
