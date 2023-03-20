# read version from installed package
from importlib.metadata import version
__version__ = version("sc_inetbox_adapter")

from .sc_inetbox_adapter import InternetboxAdapter