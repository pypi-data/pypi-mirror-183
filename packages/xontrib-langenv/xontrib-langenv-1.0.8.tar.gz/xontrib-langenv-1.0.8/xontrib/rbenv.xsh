"""Initialize rbenv at xonsh start
"""
import builtins
import os
from .langenv_common import get_bin, create_alias

__all__ = ()

RBENV = get_bin("rbenv")

# check if rbenv installed
if RBENV:
    RBENV_ENV = $(@(RBENV) init -)

    # init rbenv
    source-bash -n --suppress-skip-message @(RBENV_ENV) e>/dev/null

    create_alias("rbenv", RBENV, RBENV_ENV)
