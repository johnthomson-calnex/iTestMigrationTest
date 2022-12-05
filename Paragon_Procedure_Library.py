import importlib,sys,os, json, requests, time
from importlib.machinery import SourceFileLoader
import shutil
from datetime import datetime


from Interface import Interface
import Parameters.AllInterfaceInfo as interface_info
import Parameters.RuntimeParameters as runtime_parameters
from pathlib import Path
_instrument = ''

def load_global_parameters(parameter_file):
    global _instrument
    try:
        parameter_module = importlib.import_module(f"Parameters.{parameter_file}")
        gp = parameter_module.Global_Parameters()
        'set _instrument with the unit ip so the the p100g/p100set functions can get it'
        _instrument = gp.unit_ip
        return gp
    except Exception as e:
        print("Failed to load the parameter file correctly.")
        print(e)

def combine_parameters(global_parameters_object,test_parameters_object):
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

def setup_parameters(test_parameter_object):
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
    
def setup_check_link(interface : Interface, type : str = 'set up',couple_ports : bool = True, port : str = 'Port1'):
    print_information(f"Setting up {interface.full_interface_name} link...")
    success = True

    if type == 'set up':
        #couple/uncouple ports
        p100set(f"/api/physical/port/ethernet/group/P1P2/coupled?Coupled={couple_ports}")

        #set socket
        socket_select = get_socket_select_socket(interface)
        if socket_select == None:
            print_fail(f"Failed to get the correct socket response")
            success = False
        else:
            response = p100set(f"/api/physical/port/ethernet/{port}/socketselect?Socket={socket_select}")
            if not response.ok:
                print_fail(f"Failed to select the correct socket. ", response.json())
                success = False
            
        
        
        # set the correct interface now. also set linerate if it is not the default linerate. 
        # fec and flexe only appear in non default linerates so far so can handle them here
        if success and not 'Cxp' in interface.full_interface_name:
            endpoint = f"/api/physical/port/ethernet/{port}/{interface.interface_type}"
            if not interface.default_linerate:
                endpoint += f"?LineRate={interface.linerate}"
                if interface.has_fec:
                    endpoint += f"&Fec={interface.FecEnabled}"
                if interface.has_flexe:
                    endpoint += f"&FlexE={interface.FlexEEnabled}"
                #print(f"/api/physical/port/ethernet/{port}/{interface.interface_type}?LineRate={interface.linerate}&FlexE={interface.FlexEEnabled}&Fec={interface.FecEnabled}")
            response = p100set(endpoint)
            if not response.ok:
                print_fail(f"Failed to set the correct linerate. ",response.json())
                success = False
        
        # allow time for link
        time.sleep(12)
        

    #check for link. Try 60 times looking for 5 seconds worth of consecutive link
    if success:
        successful_links = 0
        number_attempts = 0
        max_attempts = 60
        successful_links_needed = 3
        p100set("/api/results/statusleds/reset")
        time.sleep(1)
        while number_attempts < max_attempts and successful_links < successful_links_needed:
            number_attempts += 1
            print(f"Attempt: {number_attempts}/{max_attempts}   Successful links: {successful_links}", end="\r")
            led1_response = p100get(f"/api/results/statusleds?LedNames=ethLink_0&")
            led2_response = p100get(f"/api/results/statusleds?LedNames=ethLink_1&")
            if led1_response[0]['State'] == "Link" and led2_response[0]['State'] == "Link":
                successful_links += 1
            else:
                if successful_links > 0:
                    successful_links = 0
                    print_information(f"{interface.full_interface_name} appears to have lost link while checking for {successful_links_needed} consecutive link queries")

            time.sleep(2)

            # we are one short of a complete successful link but about to stop due to max tries limit being reached so decrement number_attempts by one to give ourselves
            # one last chance to link
            if successful_links == successful_links_needed - 1 and number_attempts == max_attempts - 1:
                number_attempts -= 1

        if number_attempts == max_attempts:
            print_fail(f"Failed to establish a link for interface {interface.full_interface_name}. Tried {max_attempts} times. ")
            success = False
        
        #If we are out of the while loop and number_attempts is not equal to 60 then successful_link_tries MUST be 5


    return success
    

def get_instrument_details():
    p100set("/api/instrument/reset/default")
    print_information(f"IP Address: {runtime_parameters.unit_ip}")
    print_information(f"Unit time: {p100get('/api/instrument/systemtime')}")
    unit_info = p100get("/api/instrument/information")
    print_information(unit_info)
    runtime_parameters.isPam4 = True if 'PAM4' in unit_info['HwCapabilities'] else False
    print_information(f"Firmware version: {p100get('/api/factory/versions')['FirmwareVersion']}")
    build_version = p100get('/api/instrument/software/buildversion')['BuildVersion']
    print_information(f"Build version: {build_version}")
    runtime_parameters.build_version = build_version
    print_information(f"OS version: {p100get('/api/instrument/software/osversion')['OsVersion']}")
    options = p100get('/api/instrument/options/state')
    runtime_parameters.instrument_options = options
    print_information(f"CAT Version: {p100get('/api/cat/general/status')['VersionNumber']}")
    print_information(f"PFV Version: {p100get('/api/pfv/general/status')['VersionNumber']}")
    authenticate_smb()

def get_interfaces_on_unit():
    interfaces_available_for_test = []
    unit_interface_info = p100get(f"/api/physical/port/ethernet/group/P1P2")
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

def get_instrument_details_and_interfaces():
    #start  off by getting the instrument details and write to the console/file
    #TODO still need to write output to a file
    get_instrument_details()
    
    # Now get the interfaces on the instrument
    interfaces_on_unit = get_interfaces_on_unit()

    
    return interfaces_on_unit

def reset_ptp():
    return
    p100set("/api/results/statusleds/reset")
    p100set("/api/instrument/reset/default")
    time.sleep(2)
    p100set("/api/instrument/preset?Name=PTP 1588")
    time.sleep(1)


def authenticate_smb():
    """
    It uses the net use command to authenticate the user to the unit, this allows the test to access session files later
    """
    print_information("Authenticating SMB...")
    os.system(f"net use \\\\{runtime_parameters.unit_ip}\Calnex100G /user:calnex_user calnex_acc355!")

def apply_mask_and_create_interfaces(mask,hardware_type):
    module = importlib.import_module(f"Parameters.Interfaces_Mask")
    interfaces_on_unit = get_instrument_details_and_interfaces()
    
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

        interface_obj.FecEnabled = True if 'fec' in interface_str else False
        interface_obj.FlexEEnabled = True if 'flexe' in interface_str else False
        
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








def print_pass(message, with_newline=False):
    dtObj = datetime.now()
    timestamp = dtObj.strftime("[%D %H:%M:%S]")
    if with_newline:
        print(f"\n{timestamp}",'\u2705 ', message) 
    else:
        print(timestamp,'\u2705 ', message) 
    runtime_parameters.passes = runtime_parameters.passes + 1

    try:
        with open(f"Logging/{runtime_parameters.test_name.split('.')[0]}_{time.strftime('%D_%Hh%Mm%Ss',time.gmtime(runtime_parameters.test_start_time)).replace('/','_')}_.txt", 'a') as file:
            file.write(f"{timestamp} [Pass]  {message}\n")
    except Exception as e:
        pass

    write_to_results_xml(f"Logging/{runtime_parameters.test_name.split('.')[0]}_{time.strftime('%D_%Hh%Mm%Ss',time.gmtime(runtime_parameters.test_start_time)).replace('/','_')}.xml", timestamp, "Pass", message)

def print_fail(message, *kwargs,with_newline=False):
    dtObj = datetime.now()
    timestamp = dtObj.strftime("[%D %H:%M:%S]")
    if with_newline:
        print(f"\n{timestamp}",'\u274c ', message,*kwargs) 
    else:
        print(timestamp,'\u274c ', message,*kwargs)
    
    runtime_parameters.fails = runtime_parameters.fails + 1

    try:
        with open(f"Logging/{runtime_parameters.test_name.split('.')[0]}_{time.strftime('%D_%Hh%Mm%Ss',time.gmtime(runtime_parameters.test_start_time)).replace('/','_')}_.txt", 'a') as file:
            file.write(f"{timestamp} [Fail]  {message}\n")
    except Exception as e:
        pass
    write_to_results_xml(f"Logging/{runtime_parameters.test_name.split('.')[0]}_{time.strftime('%D_%Hh%Mm%Ss',time.gmtime(runtime_parameters.test_start_time)).replace('/','_')}.xml", timestamp, "Fail", message)

def print_information(message,with_newline=False):
    dtObj = datetime.now()
    timestamp = dtObj.strftime("[%D %H:%M:%S]")
    if with_newline:
        print(f"\n{timestamp}",'\u2139 ', message) 
    else:
        print(timestamp,'\u2139 ', message) 
    try:
        runtime_parameters.infos = runtime_parameters.infos + 1
    except: pass

    try:
        with open(f"Logging/{runtime_parameters.test_name.split('.')[0]}_{time.strftime('%D_%Hh%Mm%Ss',time.gmtime(runtime_parameters.test_start_time)).replace('/','_')}_.txt", 'a') as file:
            file.write(f"{timestamp} [Information]  {message}\n")
    except Exception as e:
        pass
    write_to_results_xml(f"Logging/{runtime_parameters.test_name.split('.')[0]}_{time.strftime('%D_%Hh%Mm%Ss',time.gmtime(runtime_parameters.test_start_time)).replace('/','_')}.xml", timestamp, "Information", message)

import xml.etree.cElementTree as ET
def write_to_results_xml(file_path,timestamp,msg,message):
    #maybe better with a path.exists check rather than try_except
    ignore = ["__builtins__","__cached__","__file__","__loader__","__name__","__package__","__spec__", "__doc__"]
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        params = tree.find("Parameters")
        execution_messages = tree.find("ExecutionMessages")
        
    except Exception as e:
        root = ET.Element("Test", Name=f"{runtime_parameters.test_name}", StartTime=time.strftime('[%D %H:%M:%S]',time.gmtime(runtime_parameters.test_start_time)), Result="NA")
        params = ET.SubElement(root,"Parameters")
        execution_messages = ET.SubElement(root,"ExecutionMessages")
        
        #[ET.SubElement(params, "Param", Param=p, Value=getattr(runtime_parameters,p)) for p in dir(runtime_parameters)]        
        for p in dir(runtime_parameters):
            if p in ignore:
                continue
            value = getattr(runtime_parameters,p)
            if isinstance(value,dict):
                parent = ET.SubElement(params, "Param", type="dict", Name=p)                
                for key in value:
                    ET.SubElement(parent, "ParamAttr",Key=key, Value=str(value[key]))
            elif isinstance(value,list):
                parent = ET.SubElement(params, "Param", type="list", Name=p)    
                for item in value:
                    ET.SubElement(parent,"ParamItem", Item=item)
            else:
                if not p == None and not value == None:  ET.SubElement(params, "Param", Type="str", Name=p, Value=str(value))
            
    #Update pass/fail/info parameters
    infos = params.find("./Param[@Name='infos']")
    passes = params.find("./Param[@Name='passes']")
    fails = params.find("./Param[@Name='fails']")

    if int(fails.attrib['Value']) > 1:
        root.set("Result", "Failed") 
    elif int(fails.attrib['Value']) == 1 and int(passes.attrib['Value']) > 0:
        root.set("Result","Passed")
    else:
        root.set("Result", "Indetermined")

    infos.attrib['Value'] = str(runtime_parameters.infos)
    passes.attrib['Value'] = str(runtime_parameters.passes)
    fails.attrib['Value'] = str(runtime_parameters.total_fails)

    

    #check for any new parameters and add to xml
    for p in dir(runtime_parameters):
        if p in ignore:
            continue
        if params.find(f"./Param[@Name='{p}']") == None:
            value = getattr(runtime_parameters,p)
            if isinstance(value,dict):
                parent = ET.SubElement(params, "Param", type="dict", Name=p)                
                for key in value:
                    ET.SubElement(parent, "ParamAttr",Key=key, Value=str(value[key]))
            elif isinstance(value,list):
                list_parent = ET.SubElement(params, "Param", type="list", Name=p)    
                for item in value:
                    ET.SubElement(list_parent,"ParamItem", Item=item)
            else:
                if not p == None and not value == None: ET.SubElement(params, "Param", Type="str", Name=p, Value=str(value))
        
    #Print messages    
    ET.SubElement(execution_messages,"Message",Type=msg, Timestamp=timestamp).text = message.__str__()
            
    
    
    
    #create the tree and write to the xml file
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(file_path)
    #time.sleep(3)
    
def print_results():
    #add any fails to total fails
    runtime_parameters.total_fails = runtime_parameters.total_fails + runtime_parameters.fails
    print("\n")
    print_pass(f"Total Passes: {runtime_parameters.passes}")
    print_information(f"Total Informations: {runtime_parameters.infos}")
    print_fail(f"Total Fails: {runtime_parameters.total_fails}")
    print("\n")
    # the print_fail call in this method will increment the fail counter by 1 and so we should check here for 1 fail rather than 0 to acount for the false fail

    if runtime_parameters.total_fails > 0:
        print_fail("Overall test result is a FAIL")
    elif runtime_parameters.total_fails == 0 and runtime_parameters.passes == 1:
        print_information("Overall test result is INDETERMINED")
    else:
        print_pass("Overall test result is a PASS")
    print("\n")

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

