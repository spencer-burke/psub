#!/usr/bin/env python3
import sys
import getpass
import re
from client import * 
#from client import Client 

def old_main():
    username = input('username: ')
    password = getpass.getpass('password: ')

    client = Client()
    logged_in = client.login(username, password)

    if not logged_in:
        print('You username or password is incorrect', file=sys.stderr, flush=True)
        exit(1)

    for challenge in client.challenges():
        print(challenge)
    
    client.work_on(101)
    print(type(client.work_on(101)))

def main():
    username = input('username: ')
    password = getpass.getpass('password: ')

    # get configuration information

    # create the session

    # use the config information with the session info to make the request
    
if __name__ == '__main__':
    pass
#    main()

