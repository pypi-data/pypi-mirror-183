# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Parzzley networking features.
"""

import os
import socket
import typing as t

if t.TYPE_CHECKING:
    import parzzley.syncengine.syncruntime


def translate_parzzley_portforwarding(machine: str, port: int,
                                      runtime: 'parzzley.syncengine.syncruntime.SyncRuntime') -> t.Tuple[str, int]:
    """
    Provides functionality for using Parzzley through an ssh remote port forwarding tunnel.
    """
    tfile = f"{runtime.datadir}/tcp_forward_{machine}.{port}"
    if os.path.isfile(tfile):
        with open(tfile, "r") as f:
            locport = int("".join(f.readlines()))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(("localhost", locport))
        portopen = result == 0
        sock.close()
        if portopen:
            return "localhost", locport
    return machine, port
