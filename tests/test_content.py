#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:26:45 2019

@author: ltetrel
"""

import unittest
import urllib.request as ulib
import tarfile
import shutil
import os
from tools.tools import dirhash

def download():
#    (tmpfile, headers) = ulib.urlretrieve("https://github.com/SIMEXP/Repo2Data/archive/multiple_data_requirement.tar.gz", "master.tar.gz")
    (tmpfile, headers) = ulib.urlretrieve("https://github.com/SIMEXP/Repo2Data/archive/master.tar.gz", "master.tar.gz")
    os.makedirs("./tests/test_in/")
    shutil.move("./master.tar.gz", "./tests/test_in/master.tar.gz")
    tar = tarfile.open("./tests/test_in/master.tar.gz", "r:gz")
    tar.extractall("./tests/test_in/")
    tar.close()
    os.remove("./tests/test_in/master.tar.gz")

class Test(unittest.TestCase):
    def test_content_equal(self):
        if os.path.exists("./tests/test_in/"):
            shutil.rmtree("./tests/test_in/")
        download()
        self.assertEqual(dirhash("./tests/test_in/Repo2Data-master"), dirhash("./tests/test_out/Repo2Data-master"))