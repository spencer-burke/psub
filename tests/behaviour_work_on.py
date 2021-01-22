import pytest
from psub import client
from pathlib import Path
import toml
import getpass

def run_behaviour_work_on():
    # create client object
    client = psub.client.Client()

    # test getting the information from the terminal while inside a pytest
    username = input('username: ')
    password = getpass.getpass('password: ')

    # authenticate and then call work_on 

    # test what work_on returns
"""
This is under development. 
I am currently looking for ways to get the password and usrname in a secure method
As pytest does really allow for input from stdin.
"""

