# get configuration information from toml file
    # resolve paths for conf file and return as valid string
    # get conf options from file and then return dictionary
import toml
import click
import os.path

def resolve_conf_path():
    """
    Returns:
        str: the string representing the path to the configuration file
    """
    result = ""
    # check for the file in .config
     
    # check for the file in ~
    # revert to /etc conf file


