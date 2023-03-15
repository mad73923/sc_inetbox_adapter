import pytest
import json
import http
from sc_inetbox_adapter.sc_inetbox_adapter import InternetboxAdapter

@pytest.fixture
def inetbox():
    with open(".password") as pwd_file:
        return InternetboxAdapter(pwd_file.readline())

@pytest.fixture
def inetbox_auth(inetbox):
    inetbox.create_session()
    return inetbox

def test_create_session(inetbox):
    status_code = inetbox.create_session()
    assert status_code == http.HTTPStatus.OK

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

def test_logout_session(inetbox_auth):
    status_code = inetbox_auth.logout_session()
    assert status_code == http.HTTPStatus.OK
