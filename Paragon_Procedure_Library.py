import importlib,sys,os, json, requests, time
import shutil
from datetime import datetime
from Command import Session

from Interface import Interface
import Parameters.AllInterfaceInfo as interface_info
import Parameters.RuntimeParameters as runtime_parameters

from pathlib import Path
from Utils_Library import write_to_results_xml, print_fail, print_information,print_pass,print_results


def load_global_parameters(parameter_file : str) -> dict:
    """
    Takes in the parameter filename and loads the file/module and returns this
    """
    try:
        parameter_module = importlib.import_module(f"Parameters.{parameter_file}")
        gp = parameter_module.Global_Parameters()
        
        return gp
    except Exception as e:
        print("Failed to load the parameter file correctly.")
        print(e)

def combine_parameters(global_parameters_object : dict,test_parameters_object : dict) -> dict:
    """
    It takes two objects and returns a dictionary with all the properties of both objects
    If there are duplicate parameter names then the local parameter will override the global parameter
    :param global_parameters: 
    :param local_parameters: 
    :return: A dictionary with all the parameters.
    """
    all_parameters = {}
    for property,value in vars(global_parameters_object).items():
        all_parameters[property] = value
    for property,value in vars(test_parameters_object).items():
        all_parameters[property] = value
    

    for key in all_parameters:
        setattr(runtime_parameters, key, all_parameters[key])

    setattr(runtime_parameters, "passes", 0)
    setattr(runtime_parameters, "fails", 0)
    setattr(runtime_parameters, "total_fails", 0)
    setattr(runtime_parameters, "infos", 0)

    setattr(runtime_parameters, "interface_test_result", True)
    setattr(runtime_parameters,"test_start_time", time.time())
    setattr(runtime_parameters,"interface_start_time", time.time())



    return all_parameters

def setup_parameters(test_parameter_object : dict) -> dict:
    """
    It takes a test parameter object and combines it with the global parameters
    
    :param test_parameter_object: a dictionary containing the test specific parameters
    :return: The return value is a dictionary of the combined parameters.
    """
    try:        
        ##FIXME removal of logging can be removed after dev
        shutil.rmtree("Logging/")
        create_results_folders()
        global_parameter_file = sys.argv[1].split(".")[0]  
        global_params = load_global_parameters(global_parameter_file)
        return combine_parameters(global_params,test_parameter_object)
    except Exception as e:
        print("Failed to create parameters for the following reason. Aborting Test.")
        print(e)
        exit()
    
def setup_interface(session : Session, interface : Interface,couple_ports : bool = True, port : str = 'Port1'):
    print_information(f"Setting up {interface.full_interface_name} link...")
    success = True

    #couple/uncouple ports
    session.put(f"/api/physical/port/ethernet/group/P1P2/coupled?Coupled={couple_ports}")

    #set socket
    socket_select = get_socket_select_socket(interface)
    if socket_select == None:
        print_fail(f"Failed to get the correct socket response")
        success = False
    else:
        response = session.put(f"/api/physical/port/ethernet/{port}/socketselect?Socket={socket_select}")
        if not response == None and 'Error' in response:
            print_fail(f"Failed to select the correct socket. ", response.json())
            success = False
        
    
    
    # set the correct interface now. also set linerate if it is not the default linerate. 
    # fec and flexe only appear in non default linerates so far so can handle them here
    if success and not 'Cxp' in interface.full_interface_name:
        endpoint = f"/api/physical/port/ethernet/{port}/{interface.interface_type}"
        if not interface.default_linerate:
            endpoint += f"?LineRate={interface.linerate}"
            if interface.fec_possible:
                endpoint += f"&Fec={interface.fec_enabled}"
            if interface.flexe_possible:
                endpoint += f"&FlexE={interface.flexe_enabled}"
            #print(f"/api/physical/port/ethernet/{port}/{interface.interface_type}?LineRate={interface.linerate}&FlexE={interface.FlexEEnabled}&Fec={interface.FecEnabled}")
        response = session.put(endpoint)
        if not response == None and 'Error' in response:
            print_fail(f"Failed to set up the specific interface. ",response.json())
            success = False

    #Check interface has been selected
    response = session.get_response(f"/api/physical/port/ethernet/{port}/{interface.interface_type}")
    
    if not response["Selected"]:
        print_fail(f"Selected interface check shows that {interface.interface_type} has not been selected")
        success = False
    if not interface.default_linerate:
        if interface.fec_possible:
            if not response["Fec"] == interface.fec_enabled:
                print_fail(f"Fec check failed for {interface.interface_type}, expected {interface.fec_enabled} but got {response['Fec']}")
                success = False
        if interface.flexe_possible:
            if not response["FlexE"] == interface.flexe_enabled:
                print_fail(f"FlexE check failed for {interface.interface_type}, expected {interface.flexe_enabled} but got {response['FlexE']}")
                success = False
    
    # allow time for link
    time.sleep(30) if runtime_parameters.isPam4 else time.sleep(15)
        

    

def check_link(session : Session, interface : Interface) -> bool:
    success = True
    #check for link. Try 60 times looking for 5 seconds worth of consecutive link
    
    successful_links = 0
    number_attempts = 0
    max_attempts = 60
    successful_links_needed = 3
    session.put("/api/results/statusleds/reset")
    time.sleep(1)
    #FIXME led_response below is givng a json error and returning None so skip for now during concept
    '''
    while number_attempts < max_attempts and successful_links < successful_links_needed:
        number_attempts += 1
        print(f"Attempt: {number_attempts}/{max_attempts}   Successful links: {successful_links}", end="\r")
        led1_response = session.get_response(f"/api/results/statusleds?LedNames=ethLink_0&")
        led2_response = session.get_response(f"/api/results/statusleds?LedNames=ethLink_1&")

        if led1_response[0]['State'] == "Link" and led2_response[0]['State'] == "Link":
            successful_links += 1
        else:
            if successful_links > 0:
                successful_links = 0
                print_information(f"{interface.full_interface_name} appears to have lost link while checking for {successful_links_needed} consecutive link queries")
        
        time.sleep(1)

        # we are one short of a complete successful link but about to stop due to max tries limit being reached so decrement number_attempts by one to give ourselves
        # one last chance to link
        if successful_links == successful_links_needed - 1 and number_attempts == max_attempts - 1:
            number_attempts -= 1

    if number_attempts == max_attempts:
        print_fail(f"Failed to establish a link for interface {interface.full_interface_name}. Tried {max_attempts} times. ")
        success = False
    '''
    #If we are out of the while loop and number_attempts is not equal to 60 then successful_link_tries MUST be 3
    return success

def get_instrument_details(session : Session) -> None:
    session.put("/api/instrument/reset/default")
    print_information(f"IP Address: {runtime_parameters.unit_ip}")
    print_information(f"Unit time: {session.get_response('/api/instrument/systemtime')}")
    unit_info = session.get_response("/api/instrument/information")
    
    runtime_parameters.isPam4 = True if 'PAM4' in unit_info['HwCapabilities'] else False
    print_information(f"Firmware version: {session.get_value('/api/factory/versions','FirmwareVersion')}")
    build_version = session.get_value('/api/instrument/software/buildversion','BuildVersion')
    print_information(f"Build version: {build_version}")
    runtime_parameters.build_version = build_version
    print_information(f"OS version: {session.get_value('/api/instrument/software/osversion','OsVersion')}")
    options = session.get_response('/api/instrument/options/state')
    runtime_parameters.instrument_options = options
    print_information(f"CAT Version: {session.get_value('/api/cat/general/status' ,'VersionNumber')}")
    print_information(f"PFV Version: {session.get_value('/api/pfv/general/status','VersionNumber')}")
    authenticate_smb()

def get_interfaces_on_unit(session : Session) -> list:
    interfaces_available_for_test = []
    unit_interface_info = session.get_response(f"/api/physical/port/ethernet/group/P1P2")
    all_interfaces_on_unit = unit_interface_info['Port1']['Interfaces']
    pam4_interfaces = ['QsfpDD','Qsfp56', 'Sfp56']
    
    for interface in all_interfaces_on_unit:
        
        if 'LineRates' in all_interfaces_on_unit[interface] or 'Qsfp28LineRate' in all_interfaces_on_unit[interface]:
            #There are multiple line rates available
            available_rates = all_interfaces_on_unit[interface]['Qsfp28LineRate']['Options'] if 'Qsfp' in interface else all_interfaces_on_unit[interface]['LineRates']['Options']
            for rate_info in available_rates:
                #Add interface and rate to list if it is in context, else print an information message to state it is not in context
                if rate_info['InContext'] == True:
                    interface_str_to_add = f"{interface}_{rate_info['Value']}"
                    if interface not in pam4_interfaces: interfaces_available_for_test.append(interface_str_to_add) 
                    has_fec = False                      
                    #check if Fec is possible for rate
                    if 'Fec' in all_interfaces_on_unit[interface]: 
                        interfaces_available_for_test.append(f"{interface_str_to_add}_fec")
                        has_fec = True
                    #check if flexE is possible for rate
                    if 'FlexE' in all_interfaces_on_unit[interface]:
                        if not 'Qsfp28_50G' in interface_str_to_add:
                            interfaces_available_for_test.append(f"{interface_str_to_add}_flexe")
                            if has_fec:
                                interfaces_available_for_test.append(f"{interface_str_to_add}_fec_flexe")
                else:
                    print_information(f"{interface} is NOT in context and will not be available to test")                
        else:
            #only one rate available
            if all_interfaces_on_unit[interface]['InContext'] == True:
                interface_str_to_add = f"{interface}"
                if interface not in pam4_interfaces: interfaces_available_for_test.append(interface_str_to_add)
                #check if Fec is possible for rate
                if 'Fec' in all_interfaces_on_unit[interface]: 
                    interface_str_to_add = f"{interface_str_to_add}_fec"
                    interfaces_available_for_test.append(interface_str_to_add)
                #check if flexE is possible for rate
                if 'FlexE' in all_interfaces_on_unit[interface]:
                    interface_str_to_add = f"{interface_str_to_add}_flexe"
                    interfaces_available_for_test.append(interface_str_to_add)
            else:
                print_information(f"{interface} is NOT in context and will not be available to test")  


    #[print(i) for i in interfaces_available_for_test]

    return interfaces_available_for_test





def reset_ptp(session : Session) -> bool:
    session.put("/api/results/statusleds/reset")
    session.put("/api/instrument/reset/default")
    time.sleep(2)
    return select_preset(session,"PTP 1588")


def select_preset(session : Session, preset : str) -> bool:
    session.put(f"/api/instrument/preset?Name={preset}")
    current_preset = session.get_value("/api/instrument/preset", "Value")
    if not current_preset == preset:
        print_fail(f"Failed to select {preset}, it is currently {current_preset}")
        return False
    else:
        return True 


def authenticate_smb():
    """
    It uses the net use command to authenticate the user to the unit, this allows the test to access session files later
    """
    print_information("Authenticating SMB...")
    os.system(f"net use \\\\{runtime_parameters.unit_ip}\Calnex100G /user:calnex_user calnex_acc355!")

def apply_mask_and_create_interfaces(session : Session, mask : str ,hardware_type : str) -> list:
    #import the parameters file to get the desired interfaces
    module = importlib.import_module(f"Parameters.Interfaces_Mask")
    
    interfaces_on_unit = get_interfaces_on_unit(session)

    mask_func = getattr(module,mask)
    
    interfaces_in_mask = mask_func()
    
    interfaces_to_test_strings = []
    interfaces_to_test = []
    
    for interface_str in interfaces_on_unit:
        if interface_str in interfaces_in_mask and interfaces_in_mask[interface_str]:
            interfaces_to_test_strings.append(interface_str)
    
    print_information("Interfaces under test " + interfaces_to_test_strings.__str__())

    for interface_str in interfaces_to_test_strings:
        interface_func = getattr(interface_info, interface_str.lower())
        interface_obj = Interface(interface_func(),hardware_type)

        
        interfaces_to_test.append(interface_obj)

    return interfaces_to_test

def get_socket_select_socket(interface):
    socket = None
    full_interface_name = interface.full_interface_name.lower()
    if "qsfp28" in full_interface_name or "qsfpplus" in full_interface_name:
        socket = "QSFP28%2FQSFP%2B&"
    elif "sfp28" in full_interface_name or "sfpplus" in full_interface_name:
        socket = "SFP28/SFP+"
    elif "sfp1g" in full_interface_name:
        socket = "SFP 1G"
    elif "SFP100m" in full_interface_name:
        socket = "SFP 100M"
    elif "rj45" in full_interface_name:
        socket = "RJ45 Low Rate"
    elif "qsfp56" in full_interface_name or "qsfpdd" in full_interface_name:
        socket = "QSFP56/QSFP-DD"
    elif "sfp56" in full_interface_name or "sfpdd" in full_interface_name:
        socket = "SFP56/SFP-DD"
    elif "cfp2dco" in full_interface_name:
        socket = "CFP2 DCO"
    elif "cxp" in full_interface_name:
        socket = "Cxp"

    
    return socket


def set_check_single_value(api_path,key,value):
    p100set(api_path, key,value)
    p100set("/api/app/mse/applypending")
    response = p100get(api_path)
    if response[key] == value:
        return True
    else:
        return False

def check_cat_results(session : Session, interface : Interface):
    pass

def check_cat_result_for_metric(session : Session, interface : Interface, delay_mech : str, name : str, port : str, metric_type : str, extId :str, statistics_id : str):
    success = False
    value = float(session.get_value(f"/api/cat/measurement/{name}/{port}/{metric_type}/{extId}/statistics/{statistics_id}", "StatisticsValue"))
    
    if delay_mech == "end_to_end":
        min_limit = interface.t1_min if name == "Sync" else interface.t4_min
        max_limit = interface.t1_max if name == "sync" else interface.t4_max        # should be capital S but leaving lowercase as it shows both pass and fail for demonstration

        if value >= min_limit and value <= max_limit:
            success = True
            print_pass(f"{name} {statistics_id} was within limits")
        else:
            print_fail(f"{name} {statistics_id} was outwith limits. Value was {value}, limits are min: {min_limit} and max {max_limit}")
    return success



def set_ethernet_cable_compensation(session : Session, interface : Interface, port : str = "Port1") -> bool :
    cable_delay = runtime_parameters.cable_compensation[interface.interface_type]
    session.put(f"/api/mse/dutethernetcabledelay?Port={port}&EthernetCableDelay={cable_delay}")
    delay = session.get_value(f"/api/mse/dutethernetcabledelay", "EthernetCableDelay")
    if not delay == cable_delay:
        print_fail(f"Failed to set the {port} cable delay for {interface.interface_type}. Expected {cable_delay} but got {delay}") 
        return False
    else:
        return True

def set_clock_reference(session : Session, use_parameter_file = True, reference = None) -> bool:
    success = True

    if use_parameter_file:
        reference = runtime_parameters.clock_reference.lower()
        if reference == "internal":
            session.put(f"/api/physical/references/in/clock/internal/select")
            ret_val = session.get_value(f"/api/physical/references/in/clock/internal", "Selected")
            if not ret_val:
                print_fail("Failed to select internal clock reference")
                success = False
        elif reference == "bnc" or reference == "external":
            session.put(f"/api/physical/references/in/clock/bnc/select")
            session.put(f"/api/physical/references/in/clock/bnc?Signal={runtime_parameters.clock_ref}")
            val =session.get_value(f"/api/physical/references/in/clock/bnc", "Signal['Value']")
            print(val)


def set_ptp_profile(session : Session, profile : str) -> bool:
    session.put(f"/api/app/mse/ptpprofile?PtpProfile={profile}")
    returned_profile = session.get_value(f"/api/app/mse/ptpprofile", "PtpProfile")
    if not returned_profile == profile:
        print_fail(f"Failed to set {profile}, it is still {returned_profile}") 
    return profile == returned_profile



def export_to_testrail(test_case_id: int, test_type : str = "interface", interface : Interface = None):
    status = "Retest"
    if test_type == "interface":
        #determine time taken for interface
        time_taken = time.time() - runtime_parameters.interface_start_time        
        run_id = runtime_parameters.run_id[interface.full_interface_name]
    elif test_type == "independant":
        run_id = runtime_parameters.run_id["independant"]
    else:
        print_fail(f"Could not determine the test_type and therefore run_id. Please ensure it is one of ['independant','interface']")
        return
    
    #need to check if we checked te results. if so then update as is but if we did not then need to retest
    if not runtime_parameters.ptp_te_check:
        if runtime_parameters.fails > 0:
            status = "Retest"
        else:
            status = "Part Pass, Retest"
    else:
        if runtime_parameters.fails > 0:
            status = "Failed, waiting on fix"
        else:
            status = "Passed"
    test_rail_api(test_case_id,status,run_id, "build id and version number etc etc")

    #now update total fails and if it is interface runs then reset the fails counter and the interface start time
    runtime_parameters.total_fails = runtime_parameters.total_fails + runtime_parameters.fails
    if test_type == "interface":
        runtime_parameters.fails = 0
        runtime_parameters.interface_start_time = time.time()


# this simulates the actual api call to testrail to export the results
def test_rail_api(test_case_id, result,run_id, rest_of_stufF_to_upload):
    print(f"About to upload to testrail. Test Case: {test_case_id}, result: {result}, run_id:{run_id}")
    

def create_results_folders():
    Path("Logging").mkdir(exist_ok=True)
    Path("Capture_Reports").mkdir(exist_ok=True)


def argsToJSON(arg):
    i = iter(arg)
    d = dict(zip(i, i))
    return json.dumps(d)

def p100get(api_path, timeout=None):
    response = requests.get("http://{0}{1}.json".format(runtime_parameters.unit_ip, api_path), timeout=timeout, headers={"Accept":"application/json"})
    
    try:
        decoded_response = response.json()
    except:
        decoded_response = response
    return decoded_response

def p100set(api_path, *arg):
    return requests.put("http://{0}{1}".format(runtime_parameters.unit_ip, api_path),
        argsToJSON(arg), headers={'Content-Type': 'application/json'})

