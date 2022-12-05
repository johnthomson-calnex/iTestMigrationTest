import sys, importlib
import Paragon_Procedure_Library

class Local_Parameters:
    
    def __init__(self):
        self.param_name = "local1"
        self.MASK = "Defaults"




def sleep_for_time():
    import time 
    print("TestCase1 sleeping for 18")
    time.sleep(18)
    print("TestCase1 wakening up")




try:
    parameters = Paragon_Procedure_Library.setup_parameters(Local_Parameters())
    print(parameters["unit_name"])   
    sleep_for_time()
except Exception as e:
    print(e)


