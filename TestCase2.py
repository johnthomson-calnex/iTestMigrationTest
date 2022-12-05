import sys, importlib
import Paragon_Procedure_Library

class Local_Parameters:
    
    def __init__(self):
        self.param_name = "local1"
        self.MASK = "Defaults"


def sleep_for_time():
    import time 
    print("TestCase2 sleeping for 10")
    time.sleep(10)
    print("testCase2 wakening up")

try:
    parameters = Paragon_Procedure_Library.setup_parameters(Local_Parameters())
    print(parameters["MASK"])   
    sleep_for_time()
except Exception as e:
    print(e)


