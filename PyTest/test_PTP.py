import pytest
import sys,os
sys.path.append(os.path.realpath("."))
from Command import Session

class test_PTP_1:

    def test_setup(self):
        self.neo = Session('192.168.204.47')
        #get interfaces for test
        assert 1 == 1

    def test_one(self):
        name = "John"
        assert "Jo" in name

    