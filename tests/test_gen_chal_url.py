import pytest
from psub import *

def test_gen_chal_url():
    # define a dictionary with the id, and proper url
    correct_urls = {
        101: "https://cse466.pwn.college/download/eyJjaGFsbGVuZ2VfaWQiOjEwMX0=",
        102: "https://cse466.pwn.college/download/eyJjaGFsbGVuZ2VfaWQiOjEwMn0=",
        105: "https://cse466.pwn.college/download/eyJjaGFsbGVuZ2VfaWQiOjEwNX0="
    }

    test_urls = {
        101: "",
        102: "",
        105: ""
    }
