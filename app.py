#!/usr/bin/env python3
import yaml
import click
from  plugins.pagure import  get_pull_requests


@click.command()
@click.option('--site', default='config', help='Please enter the sitename to list activity, e.g. github')
@click.option('--username', default='config', help='Please enter username to list activity, e.g. HariSadu')
@click.option('--repo', default='config', help='Please enter repository name to list activity, e.g. helloworld')
def execute_board(site,  username, repo):
    '''Take Arguments from command line OR Read configuration files, which is YAML format'''
    #print (site)
    #print (username) 
    if site == 'config'  and username == 'config' and repo == 'config':
          print ("The Application will read username and code sites from configuraiton file")
          with open('config.yml', 'r') as f:
             conf = yaml.load(f)

    # Expect site, username and repo comming from command line 
    #data = get_pull_requests('walters', 'fedora-atomic')
    data = get_pull_requests(username, repo)
    print (data)
   



def getComments(site, username):
     pass

def getPR(site, username):
     pass 


if __name__ == '__main__':
    click.echo("Welcome to Code Review System\n")
    execute_board()

