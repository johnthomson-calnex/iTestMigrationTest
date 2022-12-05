import requests,json,os

def argsToJSON(arg):
    i = iter(arg)
    d = dict(zip(i, i))
    return json.dumps(d)

def p100set(api_path, *arg):
    return requests.put(f"http://100g-vm4{api_path}",
        argsToJSON(arg), headers={'Content-Type': 'application/json'})


try:
    print(os.environ["itest_var"])
except Exception as e:
    print(e)