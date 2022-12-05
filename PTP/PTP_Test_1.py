
#############################################################
#                                                           #
#   Do we have the test setup and description here?         #
#   no need for it in the __init__ below?                   #
#                                                           #
#############################################################
import os,sys
sys.path.append(os.path.realpath("."))
import Paragon_Procedure_Library
import Parameters.RuntimeParameters as runtime_parameters

class Test_Parameters:
    def __init__(self):
        self.MASK = "defaults"        
        self.test_name = __file__.split("\\")[-1]
        self.test_description = "This is just a mock test to get everything up and running"
        self.test_case_id = 12345


def run():
    
    # set up parameters
    Paragon_Procedure_Library.setup_parameters(Test_Parameters())
    
    Paragon_Procedure_Library.print_information(f"Starting test {runtime_parameters.test_name}" )

    
    Paragon_Procedure_Library.reset_ptp()

    # Apply mask to interfaces
    all_interfaces_to_test = Paragon_Procedure_Library.apply_mask_and_create_interfaces(runtime_parameters.MASK, runtime_parameters.hardware_type)

    interface_error_count = 0
    
    Paragon_Procedure_Library.set_check_single_value("/api/app/mse/testmode", "TestMode", "TransparentClock")
    
    
    for interface in all_interfaces_to_test:
        Paragon_Procedure_Library.print_information(f"Testing {interface.full_interface_name}",with_newline=True)
        if not Paragon_Procedure_Library.setup_check_link(interface):
            Paragon_Procedure_Library.print_fail(f"Failed to set up a link. Skipping {interface.full_interface_name}")
            runtime_parameters.total_fails += 1
            continue
        else:
            Paragon_Procedure_Library.print_pass(f"{interface.full_interface_name} link established.")
            
        
        #Link is established so continue with test
    
        #Export to testrail
        Paragon_Procedure_Library.export_to_testrail(runtime_parameters.test_case_id, "interface", interface=interface)

    Paragon_Procedure_Library.print_pass("fake pass")

    #Print total results ie total passes/fails/informations
    Paragon_Procedure_Library.print_results()

'''
try:
    run()
except Exception as e:
    print(e)
'''

run()
