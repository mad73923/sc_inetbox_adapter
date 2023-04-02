import pytest
import json
import http
from sc_inetbox_adapter import InternetboxAdapter
from sc_inetbox_adapter import NoActiveSessionException

@pytest.fixture
def inetbox_password():
    with open(".password") as pwd_file:
        return pwd_file.readline()

@pytest.fixture
def inetbox(inetbox_password):
    return InternetboxAdapter(inetbox_password)

@pytest.fixture
def inetbox_local(inetbox_password):
    return InternetboxAdapter(inetbox_password, host="192.168.1.1", verify_ssl=False)

@pytest.fixture
def inetbox_auth(inetbox):
    inetbox.create_session()
    return inetbox

@pytest.fixture
def inetbox_local_auth(inetbox_local):
    inetbox_local.create_session()
    return inetbox_local

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
        NoActiveSessionException

def test_version(inetbox):
    ver = inetbox.get_software_version()
    assert ver == "13.20.18"

def test_device_info(inetbox_auth):
    response = inetbox_auth.get_device_info()
    print(json.dumps(response, indent=2))

def test_local_no_ssl_verify(inetbox_local_auth):
    response = inetbox_local_auth.get_device_info()

def test_logout_session(inetbox_auth):
    status_code = inetbox_auth.logout_session()
    assert status_code == http.HTTPStatus.OK
