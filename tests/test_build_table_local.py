import pytest
import os
from pathlib import Path
from psub import client

@pytest.fixture
def configure_test_paths():
    # setup file system for test fail
    p = Path.home() / '.psub.chal' 
    if(p.exists()):
        os.remove(str(p))

    p = Path.home() / '.config' / '.psub.chal' 
    if(p.exists()):
        os.remove(str(p))

def test_build_table():
    
    
