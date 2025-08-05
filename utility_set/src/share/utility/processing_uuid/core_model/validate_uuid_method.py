"""
Processing ID (core): validate id
Methods:
    check_uuid
    check_string_uuid_common
    check_string_uuid
"""

from uuid import UUID
from typing import Tuple
from re import Pattern


def check_uuid(value: UUID,
               message: str) -> Tuple[bool, bool | str, None | str]:


    pass


def check_string_uuid_common(value: str,
                             regex: Pattern,
                             message: str) -> Tuple[bool, bool | str, None | str]:

    pass


def check_string_uuid(value: str,
                      regex: Pattern,
                      message: str) -> Tuple[bool, bool | str, None | str]:

    pass
