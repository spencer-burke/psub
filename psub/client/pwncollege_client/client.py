import re

import requests


class Client:
    def __init__(self, *, url='https://cse466.pwn.college'):
        self.url = url

        self.session = requests.session()


    def login(self, username, password):
        nonce = re.search('<input id="nonce" name="nonce" type="hidden" value="(?P<nonce>.*?)">',
                          self.session.get(f'{self.url}/login').text)['nonce']

        response = self.session.post(f'{self.url}/login', data={'name': username, 'password': password, 'nonce': nonce})

        return 'Your username or password is incorrect' not in response.text


    def challenges(self):
        data = self.session.get(f'{self.url}/api/v1/challenges').json()['data']

        return [{
            'id': challenge['id'],
            'category': challenge['category'],
            'name': challenge['name'],
            'value': challenge['value']
        } for challenge in data]


    def work_on(self, challenge_id, binary = None):
        csrf = re.search('\'csrfNonce\': "(?P<csrf>.*?)"',
                         self.session.get(f'{self.url}/challenges').text)['csrf']
        if binary:
            JSON = {
                    "challenge_id": challenge_id,
                    "practice": "false",
                    "selected_path": "/bin/cat"
                    }
        else:
            JSON = {
                    "challenge_id": challenge_id,
                    "practice": "false",
                    }
            
        HEADERS = {
                'Host': 'cse466.pwn.college',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'https://cse466.pwn.college/challenges',
                'Content-Type': 'application/json',
                'CSRF-Token': csrf,
                'Origin': 'https://cse466.pwn.college'
                }

        response = self.session.post(f'{self.url}/pwncollege_api/v1/docker', headers=HEADERS, json=JSON)
        print(response)
        return response.json()['success']


    def submit_flag(self, challenge_id, flag):
        csrf = re.search('\'csrfNonce\': "(?P<csrf>.*?)"',
                         self.session.get(f'{self.url}/challenges').text)['csrf']

        JSON = {
                "challenge_id": challenge_id,
                "submission": flag
                }
        HEADERS = {
                'Host': 'cse466.pwn.college',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'https://cse466.pwn.college/challenges',
                'Content-Type': 'application/json',
                'CSRF-Token': csrf,
                'Origin': 'https://cse466.pwn.college'
                }

        response = self.session.post(f'{self.url}/api/v1/challenges/attempt', headers=HEADERS, json=JSON)

        return response.json()['success'] == True and response.json()['data']['status'] in ['correct', 'already_solved']
