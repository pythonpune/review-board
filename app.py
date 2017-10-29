#!/usr/bin/env python3
import yaml
import click

@click.command()
@click.option('--site', default='github', help='Please enter the sitename to list activity, e.g. gitgub')
@click.option('--username', default='harisadu', help='Please enter username to list activity, e.g. HariSadu')
def cmd_options(site,  username):
    print (site)
    print (username) 


if __name__ == '__main__':
    print ("Welcome to Code Review System")
    cmd_options()
