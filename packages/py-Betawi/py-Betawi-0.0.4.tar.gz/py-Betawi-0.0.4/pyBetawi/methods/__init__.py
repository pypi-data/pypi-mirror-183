from ._database import geezDB
from ._misc import _Misc
from .converter import Convert
from .func import update_envs
from .helpers import Helpers
from .hosting import where_hosted
from .Inline import InlineBot
from .queue import Queue


class Methods(
    _Misc,
    Convert,
    InlineBot,
    Helpers,
    Queue,
):
    pass
