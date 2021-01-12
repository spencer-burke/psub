import pytest
import os
from pathlib import Path

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

def test_modern_resolve_conf_path_fail():
    # setup file system for test fail
    p = Path.home() / '.config' / '.psub.toml'
    if(p.exists()):
        os.remove(str(p))


def test_modern_resolve_conf_path_pass():
    pass

def test_trad_resolve_conf_path_fail():
    pass
    
def test_trad_resolve_conf_path_pass():
    pass

def test_abs_resolve_conf_path_fail():
    pass
    
def test_abs_resolve_conf_path_pass():
    pass
    
