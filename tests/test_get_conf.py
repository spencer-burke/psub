import pytest
import toml
import psub.cli.cli 
from pathlib import Path

"""
For current testing, load the testing data each time and compare it to the already defined string.
Make sure to test all of the valid paths as all of the valid directories must be checked
Check etc readability then split if needed
"""

toml_str = """
title = "PSUB TOML configuration file"

[headers]
Host = "cse466.pwn.college"
User-Agent = "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
Accept-Language = "en-US,en;q=0.5"
Accept-Encoding = "gzip, deflate, br"
Referer = "https://cse466.pwn.college/login"
Content-Type = "application/json"
Origin = "https://cse466.pwn.college"

"""

def test_get_conf_config():
    # find the local config path
    p = Path.home() / '.config' / '.psub.toml'

    # make sure the configuration file exists 
    if (p.exists() == False):
        with open(str(p), 'w') as f:
            f.write(tom_str)

    # create a dictionary from the test data
    toml_data_test = toml.loads(toml_str)

    # create a dictionary from the config file within the config folder 
    toml_data_config = psub.cli.cli.get_conf()

    # compare the two dictionaries 
    assert toml_data_test == toml_data_config     
    
def test_get_conf_local():
    # find the home config path
    p = Path.home() / '.psub.toml'

    # make sure the configuration file exists 
    if (p.exists() == False):
        with open(str(p), 'w') as f:
            f.write(tom_str)

    # create a dictionary from the test data
    toml_data_test = toml.loads(toml_str)

    # create a dictionary from the config file within the config folder
    toml_data_config = psub.cli.cli.get_conf()

    # compare the two dictionaries 
    assert toml_data_test == toml_data_config     
     
def test_get_conf_etc():
    """
    don't make the file this time because of /etc/ write permissions
    """
    # find the etc config path
    p = Path.home() / '.config' / '.psub.toml' 

    # create a dictionary from the test data
    toml_data_test = toml.loads(toml_str)

    # create a dictionary from the config file within the config folder
    toml_data_config = psub.cli.cli.get_conf()

    # compare the two dictionaries 
    assert toml_data_test == toml_data_config     

