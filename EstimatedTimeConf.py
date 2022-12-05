import time, requests,json


def p100set(api_path, *arg):
    return requests.put("http://{0}{1}".format("192.168.204.43", api_path),
        argsToJSON(arg), headers={'Content-Type': 'application/json'})

def argsToJSON(arg):
    i = iter(arg)
    d = dict(zip(i, i))
    return json.dumps(d)

def p100get(api_path, timeout=None):
    response = requests.get("http://{0}{1}.json".format("192.168.204.43", api_path), timeout=timeout, headers={"Accept":"application/json"})
    return response

for _ in range(10000):
    res = p100get("/api/app/conformance/estimatedremainingtime")
    print(res.json()['EstimatedRemainingTime'], end="\r")
    time.sleep(0.5)

    