#!/usr/bin/env python3
import yaml
import click

@click.command()
@click.option('--site', default='config', help='Please enter the sitename to list activity, e.g. gitgub')
@click.option('--username', default='config', help='Please enter username to list activity, e.g. HariSadu')
def execute_board(site,  username):
    '''Take Arguments from command line OR Read configuration files, which is YAML format'''
    #print (site)
    #print (username) 
    if site == 'config'  and username == 'config':
          print ("The Application will read username and code sites from configuraiton file")
          with open('config.yml', 'r') as f:
             conf = yaml.load(f)
   


def getComments(site, username):
     pass

def getPR(site, username):
     pass 


if __name__ == '__main__':
    click.echo("Welcome to Code Review System\n")
    execute_board()

