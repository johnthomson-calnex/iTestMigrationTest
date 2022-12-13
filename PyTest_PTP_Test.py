import os,sys
sys.path.append(os.path.realpath("."))
import Paragon_Procedure_Library
import Parameters.RuntimeParameters as runtime_parameters
from Command import Session
from Neo_PTP_Tests import ptp_test
import Utils_Library
import pytest

class This_Test_Parameters:
    def __init__(self):
        self.MASK = "defaults"        
        self.test_name = __file__.split("\\")[-1]
        self.test_description = "This test will mimic PyTest rather than iTest"
        self.test_case_id = 12345

#FIXME how do we pass in parameter file from cmd line or find another way to specifiy global param file?
#FIXME how do we do the whole Test Case over various interfaces? can you parameterise an entire Test case rather than just individual tests - yes but can you do it at runtime?

def pytest_addoption(parser):
    parser.addoption("--param", action="store_true", help="Specifiy param file")

def pytest_generate_tests(metafunc):
    if "interface_to_test" in metafunc.fixturenames:
        if metafunc.config.getoption("param"):
            ints = ["QSFP28_100G", "QSFP28_50_Lanes0_and1"]
            metafunc.parametrize("interface_to_test", ints)


@pytest.mark.parametrize("interface", ["QSFP28_100G", "QSFP28_50_Lanes0_and1"])
class Test_Basic_PTP_Test:


    # def test_setup_parameters(self, interface_to_test):
    #     Paragon_Procedure_Library.setup_parameters(This_Test_Parameters())    
    #     self.neo = Session(runtime_parameters.unit_ip)
    #     Utils_Library.print_information(f"Starting test {runtime_parameters.test_name}" )
    #     Paragon_Procedure_Library.get_instrument_details(self.neo)

    #     assert type(self.neo) == Session , "Neo session is not correct"

    # def test_setup_clock_reference(self):
    #     assert Paragon_Procedure_Library.set_clock_reference(self.neo) == True , "Failed to set up clock reference"

    # def test_setup_ptp_profile(self):
    #     assert Paragon_Procedure_Library.set_ptp_profile(self.neo, "Profile_G_8275_1") == True, "Failed to set up PTP Profile"

    # def test_setup_interface(Self):
    #     pass

    def test_interface(self,interface):
        assert 'QSFP28' in interface, "No mention of QSFP28"