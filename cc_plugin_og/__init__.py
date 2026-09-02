import logging

from compliance_checker.base import BaseNCCheck, Result

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class OGException(Exception):
    pass


class OGChecker(BaseNCCheck):
    _cc_spec = "og"
    _cc_url = "https://oceangliderscommunity.github.io/OG-format-user-manual/OG_Format.html"
    _cc_author = "Rob Cermak, Callum Rollo"
    _cc_checker_version = __version__

    @classmethod
    def beliefs(cls):
        return {}

    @classmethod
    def make_result(cls, level, score, out_of, name, messages):
        return Result(level, (score, out_of), name, messages)

    def setup(self, ds):
        """
        Set up the OG checker by assigning the dataset

        **No validation of the attribute is performed.**

        Parameters
        ----------
        ds : netCDF4 dataset object
        """

        self.ds = ds
