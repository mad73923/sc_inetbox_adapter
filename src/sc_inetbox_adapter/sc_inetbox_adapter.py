import requests
import json
import urllib3


class Internetbox_Adapter:

    def __init__(self, admin_password: str, protocol: str = "https", ip_address: str = "192.168.1.1") -> None:
        self._admin_password = admin_password
        self._protocol = protocol
        self._ip_address = ip_address
        self._auth_token = None
        self._session = requests.Session()

    def create_session(self):
        response = self.create_context()
        #TODO check status code
        resp_json = json.loads(response.text)
        self._auth_token = resp_json['data']['contextID']
        print(response.cookies, response.headers)

    def create_context(self):
        payload = json.dumps({"service":"sah.Device.Information","method":"createContext","parameters":{"applicationName":"webui","username":"admin","password":self._admin_password}})
        headers = {
            'Authorization': 'X-Sah-Login',
        }
        return self._send_ws_request(payload, headers)

    def get_devices(self):

        payload = json.dumps({
        "service": "Devices",
        "method": "get",
        "parameters": {
            "expression": "lan and not self",
            "flags": "no_actions"
        }
        })

        response = self._send_auth_ws_request(payload)
        print(response.request.headers)

    def get_software_version(self):
        payload = json.dumps({"service":"APController","method":"getSoftWareVersion","parameters":{}})
        self._send_ws_request(payload)


    def _send_ws_request(self, payload: str, headers={}):
        url = "%s://%s/ws" % (self._protocol, self._ip_address)
        headers['Content-Type'] = 'application/x-sah-ws-4-call+json'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        #response =  requests.request("POST", url, headers=headers, data=payload, verify=False)
        response = self._session.post(url, headers=headers, data=payload, verify=False)
        print(response.text)
        return response

    def _send_auth_ws_request(self, payload: str, headers={}):
        headers['Authorization X-Sah'] = self._auth_token
        headers['X-Context'] = self._auth_token
        return self._send_ws_request(payload, headers)
