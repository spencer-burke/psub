import pytest
from psub import *

@pytest.mark.parametrize("t_input,expected", [
    (101, "https://cse466.pwn.college/download/eyJjaGFsbGVuZ2VfaWQiOjEwMX0="),
    (102, "https://cse466.pwn.college/download/eyJjaGFsbGVuZ2VfaWQiOjEwMn0="),
    (105, "https://cse466.pwn.college/download/eyJjaGFsbGVuZ2VfaWQiOjEwNX0=")
])
def test_gen_chal_url(t_input, expected):
    assert client.gen_chal_url(t_input) == expected 

