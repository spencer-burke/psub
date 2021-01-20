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
       (array(dict)): An array of dictionaries containing information on current pwncollege challenge 
    """

    data = session.get(f'{url}/api/v1/challenges').json()['data']

    return [{
        'id': challenge['id'],
        'category': challenge['category'],
        'name': challenge['name'],
        'value': challenge['value']
    } for challenge in data]

# coming back to this as it needs a lot of work
def work_on(url, session, challenge_id, binary = None, is_practice, HEADERS):
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
       ???? (???): Ok, so I think this returns a string, but I have no idea as of now
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

