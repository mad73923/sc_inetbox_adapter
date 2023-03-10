import requests
import json
import urllib3


class Internetbox_Adapter:

    def __init__(self, protocol: str = "https", ip_address: str = "192.168.1.1") -> None:
        self._protocol = protocol
        self._ip_address = ip_address

    def get_router_data(self):
        url = "%s://%s/ws" % (self._protocol, self._ip_address)

        payload = json.dumps({
        "service": "Devices",
        "method": "get",
        "parameters": {
            "expression": "lan and not self",
            "flags": "no_actions"
        }
        })
        headers = {
        'Content-Type': 'application/x-sah-ws-4-call+json'
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        print(response.text)
