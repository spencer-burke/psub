import toml
import click
from pathlib import Path

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
    Args:
        path (str): The location of the configuration file in the file system

    Returns:
        dict: A dictionary containing all of the configuration parameters
    """

    conf_path = resolve_conf_path()
    return toml.load(conf_path)
    

@click.group()
def main():
    # nothing within the main the method yet
    pass

# display all challenges(this feature will be improved later)

# login

# submit flags

# batch submit flags

# pull down a specific challenge

