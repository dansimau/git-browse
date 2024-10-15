import unittest
import subprocess
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from git import GitTestCase

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(GitTestCase))

subprocess.run(os.path.join(os.path.dirname(__file__), "createrepo.sh"))
os.chdir(os.path.join(os.path.dirname(__file__), "repo"))
unittest.TextTestRunner().run(suite)
subprocess.run(os.path.join(os.path.dirname(__file__), "destroyrepo.sh"))
