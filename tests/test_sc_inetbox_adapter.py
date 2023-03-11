import pytest
from sc_inetbox_adapter.sc_inetbox_adapter import Internetbox_Adapter

@pytest.fixture
def inetbox():
    with open(".password") as pwd_file:
        return Internetbox_Adapter(pwd_file.readline())

def test_get_context(inetbox):
    inetbox.create_context()

def test_devices(inetbox):
    inetbox.get_devices()

def test_version(inetbox):
    inetbox.get_software_version()
