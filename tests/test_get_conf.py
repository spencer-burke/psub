import pytest
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
Accept-Language = "en-US,en;q=0.5"
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
        
    # get the data
    toml_data = toml.dump(toml.load(str(p)))

# compare the two to see if the correct string is being fetched

def test_get_conf_local():
    pass

def test_get_conf_etc():
    pass

