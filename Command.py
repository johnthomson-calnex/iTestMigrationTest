import time,json,requests,datetime
from Utils_Library import write_to_results_xml
import Parameters.RuntimeParameters as runtime_parameters
from Utils_Library import print_fail
class Command():


    def __init__(self,type,api_endpoint,unit_ip):
        self.type = type
        self.api_endpoint = api_endpoint
        self.start = None
        self.end = None
        self.response = None
        self.unit_ip = unit_ip
        

    def execute(self):
        self.start = time.time()
        response = None
        if self.type == "GET":
            response = self.p100get(self.api_endpoint)
        elif self.type == "PUT":
            response = self.p100set(self.api_endpoint)
        self.end = time.time()
        self.response = response
        self.write_to_xml()
        return response

    def write_to_xml(self):
        write_to_results_xml(f"Logging/{runtime_parameters.test_name.split('.')[0]}_{time.strftime('%D_%Hh%Mm%Ss',time.gmtime(runtime_parameters.test_start_time)).replace('/','_')}.xml", time.gmtime(self.start), " ", message=None, command= self)

    def execute_return_cmd(self):
        response = self.execute()
        return response,self

    def get_duration(self):
        return self.end-self.start

    # def __str__(self):
    #     return {
    #         "type":self.type,
    #         "api_endpoint" : self.api_endpoint
    #     }

    def get_start_timestamp(self):
        return datetime.datetime.fromtimestamp(self.start)

    def get_end_timestamp(self):
        return datetime.datetime.fromtimestamp(self.end)


    def argsToJSON(self,arg):
        i = iter(arg)
        d = dict(zip(i, i))
        return json.dumps(d)

    def p100get(self,api_path, timeout=None):
        try:
            response = requests.get("{0}{1}.json".format(self.unit_ip, api_path), timeout=timeout)
            return response.json()
        except Exception as e:
            print(e)
            return None

    def p100set(self,api_path, *arg):
        try:
            requests.put("{0}{1}".format(self.unit_ip, api_path),
            self.argsToJSON(arg), headers={'Content-Type': 'application/json'}).raise_for_status()
        except Exception as e:
            print(e)
            print_fail(e)
            return None


class PUT(Command):
    def __init__(self,api_endpoint,unit_ip):
        Command.__init__(self,"PUT", api_endpoint=api_endpoint,unit_ip=unit_ip)

class GET(Command):
    def __init__(self,api_endpoint,unit_ip):
        Command.__init__(self,"GET", api_endpoint=api_endpoint,unit_ip=unit_ip)


class Session():
    def  __init__(self,unit_ip,is_https = False):
        self.ip = f"http://{unit_ip}" if not is_https else f"https://{unit_ip}"
        self.commands = []
        self.is_https = is_https

    def get_response(self,api):
        new_get_cmd = GET(api,self.ip)
        new_get_response = new_get_cmd.execute()
        self.commands.append(new_get_cmd)
        return new_get_response

    def get_value(self,api, key ):
        new_get_cmd = GET(api,self.ip)
        new_get_response = new_get_cmd.execute()
        self.commands.append(new_get_cmd)
        if key not in new_get_response:
            return f"{key} was not found in the response for {api}" 
        else:
            return new_get_response[key]

    def put(self,api):
        new_put_cmd = PUT(api,self.ip)
        new_put = new_put_cmd.execute()
        self.commands.append(new_put_cmd)
        return new_put

    def get_with_cmd(self,api):
        new_Get ,cmd= GET(api,self.ip).execute_return_cmd()
        self.commands.append(cmd)
        return new_Get, cmd
    
    def get_all_commands(self):
        return self.commands





