from argparse import Namespace
from harserver import _main
import asyncio
import requests

class Virtual_Inetbox:
    def __init__(self):
        opts = Namespace(listen='0.0.0.0', port_number=8080, debug=True, v=True)
        asyncio.run(_main(opts), debug=opts.debug)
