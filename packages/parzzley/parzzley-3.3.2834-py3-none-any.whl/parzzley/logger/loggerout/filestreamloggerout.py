# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import sys

import parzzley.logger.loggerout.abstractloggerout


class FilestreamLoggerout(parzzley.logger.loggerout.abstractloggerout.Loggerout):

    def __init__(self, filename=None):
        super().__init__()
        self.filename = filename

    def log(self, content):
        if self.filename:
            st = open(self.filename, "a")
        else:
            st = sys.stdout
        if st:  # sys.stdout might be None
            st.write(content)
            if self.filename:
                st.close()
            else:
                st.flush()

    def flush(self, wasused):
        pass
