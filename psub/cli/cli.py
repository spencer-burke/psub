import toml
import click
import requests
import getpass
from pathlib import Path
from client import *

url='https://cse466.pwn.college'   
session = requests.session() 

"""
    Get a list of return codes working
"""

def resolve_conf_path():
    """
    Returns:
        str: The string representing the path to the configuration file
    """
    
    modern_path = Path.home() / '.config' / '.psub.toml' 
    trad_path = Path.home() / '.psub.toml'
    abs_path = Path('/etc/.psub.toml')

    # check for the file in .config
    if (modern_path.exists()):
        return str(modern_path) 
    # check for the file in ~
    elif (trad_path.exists()):
        return str(trad_path) 
    # revert to /etc conf file
    elif (abs_path.exists()):
        return str(abs_path) 
    else:
        return 'NE'

def get_conf():
    """
    Returns:
        dict: A dictionary containing all of the configuration parameters
    """

    conf_path = resolve_conf_path()
    return toml.load(conf_path)

def get_headers():
    """
        Returns:
            dict: The request headers used in interacting with pwn college
    """
    params = get_conf()
    return params['headers'] 

def get_storage_path():
    """
        Returns:
            dict: The path to the storage file, to store all of the data on the challenges 
    """
    pass

def get_chal_file_path():
    """
        Returns:
            dict: The path to the storage file, to store all of the data on the challenges 
    """
    pass

if __name__ == "__main__":
    main()

def main():
    cli()

@click.group()
def cli():
    pass

@click.command() 
def display_challenges():
    # this feature will be improved later
    pass

@click.command()
def login(session):
    """
        session(Requests session object): the session that will be used to connect to pwncollege
    """
    url="https://cse466.pwn.college"
    username = input('username: ')
    password = getpass.getpass('password: ')

    client.login(url, session, username, password)

@click.command()
@click.option('--flag', help='The flag to submit')
@click.option('--batch', default=False, help='Tell the cli to batch submit flags')
def submit_flags(flag, batch, session, challenge_id, HEADERS):
    url="https://cse466.pwn.college"
    if (batch == False):
        client.submit_flag(url, session, challenge_id, flag, HEADERS)
    else:
        pass # this needs a lot of work

@click.command():
def submit_flags_batch():
    pass

@click.command()
def get_challenge():
    pass

