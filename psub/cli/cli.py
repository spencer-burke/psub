import toml
import click
import requests
from pathlib import Path

url='https://cse466.pwn.college'   
session = requests.session() 

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

# display all challenges(this feature will be improved later)
@cli.command() 
def display_challenges():
    pass

@cli.command()
def login():
    pass    

# submit flags

# batch submit flags

# pull down a specific challenge

