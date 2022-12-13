import  Parameters.RuntimeParameters as runtime_parameters
import time 
from datetime import datetime

import xml.etree.cElementTree as ET
def write_to_results_xml(file_path,timestamp,msg,message = None, command = None):
    #maybe better with a path.exists check rather than try_except
    ignore = ["__builtins__","__cached__","__file__","__loader__","__name__","__package__","__spec__", "__doc__"]
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        params = tree.find("Parameters")
        execution_messages = tree.find("ExecutionMessages")
        commands = tree.find("Commands")
        
    except Exception as e:
        root = ET.Element("Test", Name=f"{runtime_parameters.test_name}", StartTime=time.strftime('[%D %H:%M:%S]',time.gmtime(runtime_parameters.test_start_time)), Result="NA")
        params = ET.SubElement(root,"Parameters")
        execution_messages = ET.SubElement(root,"ExecutionMessages")
        commands = ET.SubElement(root, "Commands")
             
        for p in dir(runtime_parameters):
            if p in ignore:
                continue
            value = getattr(runtime_parameters,p)
            if isinstance(value,dict):
                parent = ET.SubElement(params, "Param", type="dict", Name=p)                
                for key in value:
                    ET.SubElement(parent, "DictItem",Key=key, Value=str(value[key]))
            elif isinstance(value,list):
                parent = ET.SubElement(params, "Param", type="list", Name=p)    
                for item in value:
                    ET.SubElement(parent,"ListItem", Item=str(item))
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

    try:
        print(type(runtime_parameters.run_ids))
        print("finished printing")
    except:
        pass

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
                    ET.SubElement(list_parent,"ListItem", Item=str(item))
            else:
                if not p == None and not value == None: ET.SubElement(params, "Param", Type="str", Name=p, Value=str(value))
        
    #Print messages 
    if message:   
        ET.SubElement(execution_messages,"Message",Type=msg, Timestamp=timestamp).text = message.__str__()

    #Print commads
    if command:
        cmd = ET.SubElement(commands, "Command", TimeStamp=time.strftime('[%D %H:%M:%S]',time.gmtime(command.start)))
        verb = ET.SubElement(cmd,command.type)
        api = ET.SubElement(verb, "api_endpoint")
        api.text = command.api_endpoint
        resp = ET.SubElement(verb, "Response")
        resp.text = command.response.__str__()
            
    
    
    
    #create the tree and write to the xml file
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(file_path)
    #time.sleep(3)


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
