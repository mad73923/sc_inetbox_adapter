from sc_inetbox_adapter.sc_inetbox_adapter import Internetbox_Adapter

def test_devices():
    ad = Internetbox_Adapter()
    ad.get_devices()

def test_version():
    ad = Internetbox_Adapter()
    ad.get_software_version()
