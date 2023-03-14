import pytest
import json
from sc_inetbox_adapter.sc_inetbox_adapter import InternetboxAdapter

@pytest.fixture
def inetbox():
    with open(".password") as pwd_file:
        return InternetboxAdapter(pwd_file.readline())

@pytest.fixture
def inetbox_auth(inetbox):
    inetbox.create_session()
    return inetbox

def test_get_context(inetbox):
    inetbox.create_context()

def test_create_session(inetbox):
    status_code = inetbox.create_session()
    assert status_code == 200

def test_devices(inetbox_auth):
    response = inetbox_auth.get_devices()
    print(json.dumps(response, indent=2))

def test_non_auth_call(inetbox):
    try:
        response = inetbox.get_devices()
    except:
        Exception()

def test_version(inetbox):
    ver = inetbox.get_software_version()
    assert ver == "13.20.18"

def test_release_context(inetbox_auth):
    inetbox_auth.release_context()
