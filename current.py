import os
import re
import json
import subprocess
import requests # get a venv going for this and remove this comment afterwards

DOMAIN = 'cse.466.pwn.college'
CHALL_FILE = './challs.json'

class Web(object):
    """
    Module to interact with the pwn college infrastructure
    """
    def __init__(self, cookie):
        self.session = requests.Session()
        self.session.cookies.set(domain=DOMAIN, name='session', value=cookie)
        self.url = 'https://%s' % DOMAIN
        self.challs = self.challenges()
        self.csrf_token = self.get_csrf_token()

    def get_csrf_token(self):
        """
        get csrf token for other api usage
        """

        content = self.session.get(self.url+'/challenges').text
        token = re.search('csrf_nonce = "[0-9a-f]+)"', content).group(1)
        return token

    def challenges(self):
        """
        get all challenges
        """

        # fetch from cache
        if os.path.exists(CHALL_FILE):
            with open(CHALL_FILE) as f:
                return json.load(f)

        r = self.session.get(self.url+'/api/v1/challenges')
        res = r.json()
        assert res['success']
        return res['data']

    def workon(self, thing, practice=False):
        """
        workon a challenge
        """

        if isinstance(thing, int):
            challenge_id = thing
        elif isinstance(thing, str):
            for chall in self.challs:
                if thing != chall['name']:
                    continue
                challenge_id = int(chall['id'])
                break
        else:
            raise ValueError('oops')
        url = self.url + 'pwncollege_api/v1/docker'
        header = {'csrf-token': self.csrf_token}
        data = {'challenge_id': challenge_id, 'practice': practice}

        res = self.session.post(url, headers=header, json=data).json()
        assert res['success']
        return

    def submit(self, challenge_id, flag):
        """
        download one single challenge binary into a local folder
        """

        print('Downloading %s' % chall['name'])
        subprocess.call(["scp", "-i", os.path.expanduser("~/.ssh/id_rsa"), "cse466@cse466.pwn.college:%s" % path, folder])
        assert os.path.exists(os.path.join(folder, os.path.basename(path)))

if __name__ == '__main__':
    import sys

    web = Web('xxxxxx')
    json.dump(web.challs, indent=4))

    download_challs = [x for x in web.challs if x['category'] == 'babyheap']
    for chall in download_challs:
        web.download_one_chall(chall, './challs')
    # somewhat of a proof of concept for submitting a challenge as well
    web.submit('example_id', 'example_flag')

