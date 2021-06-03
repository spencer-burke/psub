import re
import toml
import base64
import requests
from requests.auth import HTTPBasicAuth

class Client:
    pass

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

    Returns:
       (array(dict)): An array of dictionaries containing information on current pwncollege challenge 
    """

    data = session.get(f'{url}/api/v1/challenges').json()['data']

    return [{
        'id': challenge['id'],
        'category': challenge['category'],
        'name': challenge['name'],
        'value': challenge['value']
    } for challenge in data]

def build_table(url, session, storage_file):
    """
    Args:
        url (str): The url to connect to
        session (requests session object): The requests session object being used for the connection
        storage_file (str): the absolute path containing the name of the storage file where the information for all of the challenges will be kept
    """ 
    chals = challenges(url, session)
    toml_string = toml.dump(chals)
    with open(storage_file, "a") as f:
       f.write(toml_string) 

# coming back to this as it needs a lot of work
def work_on(url, session, challenge_id, is_practice, HEADERS, binary = None):
    """
    Args:
        url (str): The url to connect to
        session (requests session object): The requests session object being used for the connection
        challenge_id (str): The id of the challenge to work on
        binary (dict): The binary challenge dictionary which contains all of the information needed to work on a binary challenge
        ^^^ this is currently in the works, the dict will have the challenge_id 
        ^^^ the selected_path of the challenge binary(this feature might not even be implemented as the pwncollege infrastructure might change)
        is_practice (boolean): Whether the challenge being worked on is a practice challenge or a test challenge
        HEADERS (dict): The headers needed to make the request to work on the challenge

    Returns:
       bool: whether the request was successful 
    """

    csrf = re.search('\'csrfNonce\': "(?P<csrf>.*?)"',
                     session.get(f'{url}/challenges').text)['csrf']

    practice = ""

    if(is_practice):
        practice = "false"  
    else:
        practice = "true"

    if binary:
        JSON = {
                "challenge_id": challenge_id,
                "practice": practice,
                "selected_path": "/bin/cat"
                }
    else:
        JSON = {
                "challenge_id": challenge_id,
                "practice": practice,
                }
    
    response = session.post(f'{url}/pwncollege_api/v1/docker', headers=HEADERS, json=JSON)
    print(response)

    # this needs to be removed
    print(type(response.json()['success']))
    return response.json()['success']

def gen_chal_url(challenge_id):
    """
    Args:
        challenge_id (int): The challenge id that is going to be requested

    Returns:
        str: The url to make the request to for the challenge
    """

    pwn_url_part = "https://cse466.pwn.college/download/"
    
    challenge_str = "{\"challenge_id\":%d}" % (challenge_id)
    challenge_str_bytes = base64.urlsafe_b64encode(challenge_str.encode("utf-8"))
    challenge_str_decoded = pwn_url_part + str(challenge_str_bytes, "utf-8")

    return challenge_str_decoded

# two functions are being made as of now to make functionality easier, and to prototype funcitonality easier
def work_on_chal(url, session, challenge_id, HEADERS, is_practice=False):
    """
    Args:
        url (str): The url to connect to (this might not be used)
        session (requests session object): The requests session object being used for the connection
        challenge_id (str): The id of the challenge to work on
        is_practice (boolean): Whether the challenge being worked on is a practice challenge or a test challenge
        HEADERS (dict): The headers needed to make the request to work on the challenge

    Returns:
        bool: whether the request was successful or not 
    """

    csrf = re.search('\'csrfNonce\': "(?P<csrf>.*?)"', session.get(f'{url}/challenges').text)['csrf']
    HEADERS['CSRF-Token'] = csrf
    
    response = session.get(gen_chal_url(challenge_id), headers=HEADERS, allow_redirects=True)
    with open(str(challenge_id), 'w') as f:
        f.write(str(response.content))

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

    HEADERS['CSRF-Token'] = csrf

    JSON = {
            "challenge_id": challenge_id,
            "submission": flag
            }
    
    response = session.post(f'{url}/api/v1/challenges/attempt', headers=HEADERS, json=JSON)

    # this returns whether the flag was correct or already solved
    #return response.json()['success'] == True and response.json()['data']['status'] in ['correct', 'already_solved']
    print(response.json())
