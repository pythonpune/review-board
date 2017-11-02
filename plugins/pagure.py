from libpagure import Pagure
import utils

@utils.safe_error_decorator
def get_pull_requests(username, repository_name):
    """
    Returns the list of PR titles for specified username and repo from Pagure
    :param username: username of the user on Pagure
    :param repository_name: name of the repo on Pagure
    :returns: List of titles of PRs
    """
    pg = Pagure()
    pg.repo= repository_name
    list_of_pull_requests = []
    for pull_request in pg.list_requests():
        if pull_request["user"]["name"] == username:
            list_of_pull_requests.append(pull_request["title"])
    
    return list_of_pull_requests

# print(get_pull_requests('walters', 'fedora-atomic'))
