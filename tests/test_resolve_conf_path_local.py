import pytest
import os
from pathlib import Path
import psub.cli.cli 

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

@pytest.fixture
def configure_test_paths():
    # setup file system for test fail
    p = Path.home() / '.psub.toml' 
    if(p.exists()):
        os.remove(str(p))

    p = Path.home() / '.config' / '.psub.toml' 
    if(p.exists()):
        os.remove(str(p))
    
def test_resolve_conf_path_fail(configure_test_paths):
   assert psub.cli.cli.resolve_conf_path() == 'NE'

def test_modern_resolve_conf_path_pass(configure_test_paths):
    p = Path.home() / '.config' / '.psub.toml'

    with open(str(p), 'w') as f:
        f.write(toml_str)
    
    assert psub.cli.cli.resolve_conf_path() == str(p)
    
def test_trad_resolve_conf_path_pass(configure_test_paths):
    p = Path.home() / '.psub.toml'

    with open(str(p), 'w') as f:
        f.write(toml_str)

    assert psub.cli.cli.resolve_conf_path() == str(p)

