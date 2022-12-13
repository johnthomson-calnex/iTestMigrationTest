import os,sys
sys.path.append(os.path.realpath("."))
import Paragon_Procedure_Library
import Parameters.RuntimeParameters as runtime_parameters
from Command import Session
from Neo_PTP_Tests import ptp_test
import Utils_Library

class Test_Parameters:
    def __init__(self):
        self.MASK = "defaults"        
        self.test_name = __file__.split("\\")[-1]
        self.test_description = "This test will mimic iTest rather than PyTest"
        self.test_case_id = 12345


def run():

    # setup parameters and create the session
    Paragon_Procedure_Library.setup_parameters(Test_Parameters())    
    neo = Session(runtime_parameters.unit_ip)
    Utils_Library.print_information(f"Starting test {runtime_parameters.test_name}" )
    Paragon_Procedure_Library.get_instrument_details(neo)

    #Reset to PTP Preset
    Paragon_Procedure_Library.reset_ptp(neo)


    all_interfaces_to_test = Paragon_Procedure_Library.apply_mask_and_create_interfaces(neo,runtime_parameters.MASK, runtime_parameters.hardware_type)

    for interface_under_test in all_interfaces_to_test:
        interface_passed = ptp_test(neo, interface_under_test, encapsulation="Ethernet")

        if interface_passed:
            Utils_Library.print_pass(f"{interface_under_test.full_interface_name} PASSED")
        else:
            Utils_Library.print_fail(f"{interface_under_test.full_interface_name} FAILED \n")
        







run()