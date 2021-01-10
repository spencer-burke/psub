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
    conf_path_modern = '~/.config/.psub.toml'
    conf_path_traditional = '~/.psub.toml'
    conf_path_absolute = '/etc/psub.toml'

    # check for the file in .config
    path = Path(conf_path_modern) 
    if (path.exists()):
        return conf_path_modern
    # check for the file in ~
    path = Path(conf_path_traditional)
    elif (path.exists()):
        return conf_path_traditional
    # revert to /etc conf file
    path = Path(conf_path_absolute)
    elif (path.exists()):
        return conf_path_absolute
    else:
        return 'NAN'

def get_conf(path):
    """
    Args:
        path (str): The location of the configuration file in the file system

    Returns:
        dict: A dictionary containing all of the configuration parameters
    """
    
    pass


