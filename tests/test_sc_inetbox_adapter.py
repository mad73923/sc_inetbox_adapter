import pytest
from sc_inetbox_adapter.sc_inetbox_adapter import Internetbox_Adapter

@pytest.fixture
def inetbox():
    with open(".password") as pwd_file:
        return Internetbox_Adapter(pwd_file.readline())

@pytest.fixture
def inetbox_auth(inetbox):
    inetbox.create_session()
    return inetbox

def test_get_context(inetbox):
    inetbox.create_context()

def test_devices(inetbox_auth):
    inetbox_auth.get_devices()

def test_version(inetbox):
    inetbox.get_software_version()
