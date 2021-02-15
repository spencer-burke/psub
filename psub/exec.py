#!/usr/bin/env python3
import sys
import getpass
import re
from client import * 
from cli import *
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

    conf = cli.get_conf()
    pwn_session = requests.session()
    pwn_url = "https://cse466.pwn.college"

    client.login(pwn_url, pwn_session, username, password)

    # use the config information with the session info to make the request
    client.work_on_chal(pwn_url, pwn_session, 101, conf)
    # attempt to submit a flag
    client.submit_flag(pwn_url, pwn_session, "pwn_college{MK9noUdT-C1gNN5Spyd6IqDUexB.dFDMxwCN4UzW}", conf)
    
if __name__ == '__main__':
    main()

