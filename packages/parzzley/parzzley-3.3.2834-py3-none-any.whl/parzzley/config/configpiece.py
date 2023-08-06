# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Helpers for Parzzley configuration handling.
"""

import datetime
import typing as t

import parzzley.config.config
import parzzley.exceptions


def gettimedelta(s: t.Any) -> datetime.timedelta:
    """
    If `s` is a `datetime.timedelta`, it is returned directly, otherwise it is parsed from string.
    """
    if isinstance(s, datetime.timedelta):
        return s
    else:
        unit = s[-1]
        value = float(s[:-1])
        if unit == "s":
            seconds = value
        elif unit == "m":
            seconds = value * 60
        elif unit == "h":
            seconds = value * 60 * 60
        elif unit == "d":
            seconds = value * 60 * 60 * 24
        else:
            raise parzzley.exceptions.ReadInvalidConfigurationError("unknown or no unit given in timedelta: " + s)
        return datetime.timedelta(seconds=seconds)


def getbool(s: t.Any) -> bool:
    """
    If `s` is a `bool`, it is returned directly, otherwise it is parsed from string.
    """
    if isinstance(s, bool):
        return s
    else:
        return s == "1"


def getcallable(s: t.Any, argnames: t.List[str]) -> t.Callable:
    """
    If `s` is a `callable`, it is returned directly, otherwise it is parsed from string.
    """
    if callable(s):
        return s
    else:
        g = parzzley.config.config.threadlocal.knowntypes[-1]
        def _callable(**kwa):
            gg = dict(g)
            for argname in argnames:
                gg[argname] = kwa[argname]
            return eval(s, gg, gg)
        return _callable


def getlist(kwa: t.Dict[str, t.Optional[t.Any]], listname: str) -> t.List[str]:
    """
    Returns a list from a keyword-args structure either by direct lookup or by flattened lookup
    (`foo_0`, `foo_1`, `foo_2`, ..., `foo_n`).
    """
    if listname in kwa:
        return kwa.pop(listname)
    result = []
    i = 0
    while f"{listname}_{i}" in kwa:
        result.append(kwa.pop(f"{listname}_{i}"))
        i += 1
    return result
