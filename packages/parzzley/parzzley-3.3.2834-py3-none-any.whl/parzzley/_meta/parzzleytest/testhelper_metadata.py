# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Some helper functions for implementing tests about metadata handling.
"""


import os
import xattr
# noinspection PyPep8Naming
import xml.etree.cElementTree as ET


class Metadata:

    def __init__(self, mydir):
        self.mydir = mydir

    def setfilemetadata(self, p, k, v):
        _p = self.mydir + p
        xattr.set(_p, f"user.parzzleytest_{k}", v)

    def getfilemetadata(self, p, k):
        _p = self.mydir + p
        try:
            # noinspection PyUnresolvedReferences
            return xattr.get(_p, f"user.parzzleytest_{k}").decode("utf-8")
        except Exception:
            return None

    def getshadowmetadata(self, p, k, hint_isdir=None):
        isdir = os.path.isdir(self.mydir + p) or hint_isdir
        shadowfullpath = os.path.abspath(self.mydir + p[0:p.find("/")] + "/.parzzley.control/content_metadata")
        xmlpath = shadowfullpath + "/" + p[p.find("/")+1:] + ("/##parzzley.directory.metadata##" if isdir else "")
        if os.path.isfile(xmlpath):
            root = ET.parse(xmlpath).getroot()
            if k == "_version":
                return root.attrib["version"]
            for xmlchild in root:
                if xmlchild.attrib["key"] == k:
                    return xmlchild.attrib["value"]
        else:
            return None

    def setshadowmetadata(self, p, k, v):
        isdir = os.path.isdir(self.mydir + p)
        shadowfullpath = os.path.abspath(self.mydir + p[0:p.find("/")] + "/.parzzley.control/content_metadata")
        xmlpath = shadowfullpath + "/" + p[p.find("/")+1:] + ("/##parzzley.directory.metadata##" if isdir else "")
        root = ET.parse(xmlpath).getroot()
        root.attrib["version"] = str(int(root.attrib["version"])+1)
        for xmlchild in root:
            if xmlchild.attrib["key"] == k:
                xmlchild.attrib["value"] = v
        with open(xmlpath, "w") as f:
            f.write(ET.tostring(root).decode())

    def killshadowmetadata(self, p):
        isdir = os.path.isdir(self.mydir + p)
        shadowfullpath = os.path.abspath(self.mydir + p[0:p.find("/")] + "/.parzzley.control/content_metadata")
        xmlpath = shadowfullpath + "/" + p[p.find("/")+1:] + ("/##parzzley.directory.metadata##" if isdir else "")
        os.unlink(xmlpath)
