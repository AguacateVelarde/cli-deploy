import click
import requests
from helpers import name
from steps_funtions import core_deploy, core_copy
import variables
__author__ = "Leonardo Velarde"

@click.group()
def main():
    name()    

@main.command()
@click.option(
    '--path', '-p', 
    default=variables.default_path, 
    help='Folder path to run ng build.'
)
@click.option(
    '--build', '-b', 
    default=variables.default_build_command, 
    help='Command for build project.'
)
@click.option(
    '--copy', '-c',
    is_flag=True,
    help='Flag to copy login files to specific path.'
)
@click.option(
    '--endpath', '-ep',
    default=variables.default_destiny_folder_copy, 
    help='Folder path to copy files.'
    
)
def deploy(path, build, copy, endpath):
    '''
        Build aplication run ng build
        and copy files using flag --copy or -c
    '''
    core_deploy(path, build)
    if copy :
        core_copy(path, endpath)


@main.command()
@click.option(
    '--path', '-p', 
    default=variables.default_path, 
    help='Folder path to run ng build.'
)
@click.option(
    '--endpath', '-ep',
    default=variables.default_destiny_folder_copy, 
    help='Folder path to copy files.'
)
def copy(path, endpath):
    '''
        Copy files only 
    '''
    core_copy(path, endpath)

if __name__ == "__main__":
    main()