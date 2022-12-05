import os,sys
sys.path.append(os.path.realpath("."))
import Paragon_Procedure_Library

class Test_Parameters:
    def __init__(self):
        self.MASK = "STC"
        self.rj45_cable_comp = 2.223



def run():
    # set up parameters
    parameters = Paragon_Procedure_Library.setup_parameters(Test_Parameters())
    
    print(parameters["MASK"])

    
try:
    run()
except Exception as e:
        print(e)
