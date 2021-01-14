import pytest
import os
from pathlib import Path
import psub.cli.cli 

"""
If you are running this test you must make sure to run it in an elevated environment.
Since it is checking for a file in /etc/.
Also, run the test with the "/etc/.psub.toml" file not existing.
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
 
def test_abs_resolve_conf_path_pass():

    with open('/etc/.psub.toml', 'w') as f:
        f.write(toml_str)

    assert psub.cli.cli.resolve_conf_path() == '/etc/.psub.toml' 
