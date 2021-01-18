import re
import requests

def login(url, session, username, password):
    """
    Args:
        url (str): The url to connect to
        session (requests session object): The requests session object being used for the connection
        username (str): the username being used to authenticate to pwncollege
        password (str): the password being used to authenticate to pwncollege

    Returns:
        boolean: whether the authentication was successful
    """

    nonce = re.search('<input id="nonce" name="nonce" type="hidden" value="(?P<nonce>.*?)">',
                      session.get(f'{url}/login').text)['nonce']

    response = session.post(f'{url}/login', data={'name': username, 'password': password, 'nonce': nonce})

    return 'Your username or password is incorrect' not in response.text

def challenges(url, session):
    """
    Args:
        url (str): The url to connect to
        session (requests session object): The requests session object being used for the connection
        username (str): the username being used to authenticate to pwncollege
        password (str): the password being used to authenticate to pwncollege

    Returns:
        boolean: whether the authentication was successful
    """

    data = session.get(f'{url}/api/v1/challenges').json()['data']

    return [{
        'id': challenge['id'],
        'category': challenge['category'],
        'name': challenge['name'],
        'value': challenge['value']
    } for challenge in data]

# coming back to this as it needs a lot of work
def work_on(challenge_id, binary = None):
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

def submit_flag(url, session, challenge_id, flag, HEADERS):
    """
    Args:
        url (str): The url to connect to
        session (requests session object): The requests session object being used for the connection
        challenge_id (str): the id of the challenge that the flag is for 
        flag (str): the flag being submitted 
        HEADERS (dict): the headers being used to make the request when submitting the flag

    Returns:
        boolean: whether the flag was correct or already solved 
    """

    csrf = re.search('\'csrfNonce\': "(?P<csrf>.*?)"',
                         session.get(f'{url}/challenges').text)['csrf']

    JSON = {
            "challenge_id": challenge_id,
            "submission": flag
            }
    
    response = session.post(f'{url}/api/v1/challenges/attempt', headers=HEADERS, json=JSON)

    # this returns whether the flag was correct or already solved
    return response.json()['success'] == True and response.json()['data']['status'] in ['correct', 'already_solved']

