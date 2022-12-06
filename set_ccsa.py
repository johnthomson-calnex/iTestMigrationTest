#https://www.github.com/johnthomson-calnex/iTestMigrationTest.git

import requests,json,os,sys

def argsToJSON(arg):
    i = iter(arg)
    d = dict(zip(i, i))
    return json.dumps(d)

def p100set(api_path,ip, *arg):
    return requests.put(f"http://{ip}{api_path}",
        argsToJSON(arg), headers={'Content-Type': 'application/json'})


try:
    ip = os.environ["ip"]
    #ip = '100g-vm1'
    #ip = sys.argv[1]
    p100set("/api/app/mse/ptpprofile?PtpProfile=Profile_CCSA", ip)

    exit(0)
    
except Exception as e:
    print(e)
    exit(1)