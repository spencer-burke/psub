#!/usr/bin/env python3
import sys
import getpass
import re

import pwncollege_client

def main():
    username = input('username: ')
    password = getpass.getpass('password: ')

    client = pwncollege_client.Client()
    logged_in = client.login(username, password)

    if not logged_in:
        print('You username or password is incorrect', file=sys.stderr, flush=True)
        exit(1)

    for challenge in client.challenges():
        print(challenge)

if __name__ == '__main__':
    main()

