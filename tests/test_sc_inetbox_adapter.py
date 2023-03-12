import pytest
from sc_inetbox_adapter.sc_inetbox_adapter import Internetbox_Adapter
from virtual_inetbox import Virtual_Inetbox

@pytest.fixture
def inetbox(request):
    if request.config.getoption("--local"):
        with open(".password") as pwd_file:
            yield Internetbox_Adapter(pwd_file.readline())
    else:
        vbox = Virtual_Inetbox()
        yield Internetbox_Adapter("test123", ip_address="127.0.0.1:32443")

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
    inetbox_auth.get_devices()

def test_version(inetbox):
    ver = inetbox.get_software_version()
    assert ver == "13.20.18"

def test_release_context(inetbox_auth):
    inetbox_auth.release_context()
