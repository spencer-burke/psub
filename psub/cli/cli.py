# get configuration information from toml file
    # resolve paths for conf file and return as valid string
    # get conf options from file and then return dictionary
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
    abs_path = Path(conf_path_absolute)

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

def get_conf(path):
    """
    Args:
        path (str): The location of the configuration file in the file system

    Returns:
        dict: A dictionary containing all of the configuration parameters
    """
    
    pass

