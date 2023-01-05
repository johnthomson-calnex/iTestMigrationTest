import os,sys,requests,importlib,time
sys.path.append(os.path.realpath("."))
import Paragon_Procedure_Library
import Parameters.RuntimeParameters as runtime_parameters
from Command import Session
from Neo_PTP_Tests import ptp_test
import Utils_Library
import pytest
from Neo_Procedure_Library import get_interfaces
class This_Test_Parameters:
    def __init__(self):
        self.MASK = "defaults"        
        self.test_name = __file__.split("\\")[-1]
        self.test_description = "This test will mimic PyTest rather than iTest"
        self.test_case_id = 12345

#FIXME how do we pass in parameter file from cmd line or find another way to specifiy global param file?
#FIXME how do we do the whole Test Case over various interfaces? can you parameterise an entire Test case rather than just individual tests - yes but can you do it at runtime?

#FIXME if it is parameterized then you MUST include the parameter in the function , even setup_clock_ref would need to take in interface even tho it will not be used
#FIXME also every single test runs for each interface and so it may be difficult to have 'set up' and 'tear down' functions
#FIXME in the example of ptp_tests, it doesn't really make sense to have one big function with different parameters, this means that the code in that function will need 'copied' to every ptp test etc
#FIXME cannot print to the console so may be more difficult for development - you can use -s flag but still not exactly convenient (sys.stdout.write() or print())
    


@pytest.mark.parametrize("interface", get_interfaces())
class Test_Basic_PTP_Test:

    @pytest.fixture(scope="session",autouse=True)
    def set_up(self):
        self.ip = "http://100g-vm7"
        self.put("/api/app/mse/ptpprofile?PtpProfile=Profile_G_8265_1", self.ip)
        yield
        None
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

    def test_interface_for_QSFP28(self,interface):
        time.sleep(5)
        if interface == "Qsfp28_100G":
            pytest.skip("Don't want this one " + interface + " ")
        sys.stdout.write("output here " + interface + " ")
        assert 'Qsfp28' in interface, "No mention of QSFP28"

    #  def test_interface_for_SFP1G1(self,interface):
    #      assert 'SFP1G' in interface, "No mention of SFP1G"

    # def test_interface_for_SFP1G(self,interface):
    #     assert 'SFP1G' in interface, "No mention of SFp1G"
    
    # def test_interface_for_SQSFP28(self,interface):
    #     assert 'QSFP28' in interface, "No mention of QSFP28"
    
    # def test_interface_for_SFP1G2(self,interface):
    #     assert 'SFP1G' in interface, "No mention of SFp1G"

    # def put(self,api):
    #     requests.put("{0}{1}".format("http://100g-vm9", api), headers={'Content-Type': 'application/json'}).raise_for_status()

    # def test_z(self):
    #     self.put("/api/app/mse/ptpprofile?PtpProfile=Profile_G_8275_1")
    
    # def test_lessthan4(self):
    #     x = 5
    #     assert x < 4, f"x not less than 4 as x is {x}"

    # def test_b(self):
    #     self.put("/api/app/mse/ptpprofile?PtpProfile=Profile_G_8265_1")
    
    # def test_y(self):
    #     self.put("/api/app/mse/ptpprofile?PtpProfile=Profile_802_1AS")
    
    # def test_d(self):
    #     self.put("/api/app/mse/ptpprofile?PtpProfile=Profile_1588_2008_Annex_J")

    

    # def test_greaterthan4(self):
    #     x = 5
    #     assert x > 4, "x not greater than 4"

    def put(self,api,ip):
        requests.put("{0}{1}".format(ip, api), headers={'Content-Type': 'application/json'}).raise_for_status()

    @pytest.fixture(scope="session",autouse=True)
    def tear_down(self):
        None
        yield
        self.put("/api/app/mse/ptpprofile?PtpProfile=Profile_G_8275_1", self.ip)


with open('f.txt', 'w') as f:
    f.write("something")