#!/bin/python3
import pytest
import os
from pathlib import Path
from psub import client
from psub import cli

@pytest.fixture
def configure_test_paths():
    # setup file system for test fail
    p = Path.home() / '.psub.chal' 
    if(p.exists()):
        os.remove(str(p))

    p = Path.home() / '.config' / '.psub.chal' 
    if(p.exists()):
        os.remove(str(p))

def test_resolve_chal_path_modern():
    modern_path = Path.home() / '.config' / '.psub.chal' 
    assert psub.cli.resolve_chal_path_no_config() == modern_path

