#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:26:45 2019

@author: ltetrel
"""

import unittest
from tools import dirhash
import urllib.request as ulib
import tarfile

def download():
#    (tmpfile, headers) = ulib.urlretrieve("https://github.com/SIMEXP/Repo2Data/archive/multiple_data_requirement.tar.gz", "master.tar.gz")
    (tmpfile, headers) = ulib.urlretrieve("https://github.com/SIMEXP/Repo2Data/archive/master.tar.gz", "master.tar.gz")
    tar = tarfile.open("master.tar.gz", "r:gz")
    tar.extractall()
    tar.close()

class Test(unittest.TestCase):

    def test_content_equal(self):
        download()
        self.assertEqual(dirhash("Repo2Data-master"), dirhash("./test_in/Repo2Data-master"))
        
if __name__ == '__main__':
    unittest.main()